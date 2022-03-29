import imp
import datetime
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from itertools import chain

from core.functions import generate_form_errors, get_response_data
from .models import Loan
# Create your views here.

@login_required
def pending_loan_requests(request):
    if request.user.is_superuser:
        query_set = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            global_manager_approved=True
        )
    if request.user.is_global_manager:
        query_set = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            manager_approved=True
        )
    elif request.user.is_sales_manager:
        query_set = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            creator__region=request.user.region
        )
    elif request.user.is_sales_coordinator:
        query_set = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=True,
            creator__region=request.user.region
        )
    elif request.user.is_sales_supervisor:
        qs = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False,
        ).prefetch_related('creator')
        exe_qs = qs.filter(creator__salesexecutive__supervisor__user=request.user)
        mer_qs = qs.filter(creator__merchandiser__executive__supervisor__user=request.user)
        query_set = chain(exe_qs,mer_qs)
    context = {
        "title": "Pending Loan requests",
        "instances": query_set,
    }
    return render(request,"loan/pending_loan.html", context)


@login_required
def loan_single(request, pk):
    instance = get_object_or_404(Loan, pk=pk)
    context = {
        "title": "Loan single page ",
        "instance": instance,
    }
    return render(request, "loan/single.html", context)



@login_required
def accept_loan(request, pk):
    loan = get_object_or_404(Loan,pk=pk)

    if request.user.is_superuser:
        loan.is_approved = True
        loan.is_rejected = False
        loan.save()
    if request.user.is_global_manager:
        loan.is_approved = True
        loan.is_rejected = False
        loan.global_manager_approved = True
        loan.save()
    if request.user.is_sales_manager:
        loan.is_approved = True
        loan.is_rejected = False
        loan.manager_approved = True
        loan.save()
    elif request.user.is_sales_coordinator:
        loan.is_approved = True
        loan.is_rejected = False
        loan.coordinator_approved = True
        loan.save()
    elif request.user.is_sales_supervisor:
        loan.supervisor_approved = True
        loan.supervisor_rejected = False
        loan.save()

    response_data = get_response_data(
        1, redirect_url=reverse("loans:accepted_loans"), message="Approved"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def reject_loan(request, pk):
    loan = get_object_or_404(Loan,pk=pk)

    if request.user.is_superuser:
        loan.is_approved = False
        loan.is_rejected = True
        loan.save()
    if  request.user.is_global_manager:
        loan.is_approved = False
        loan.is_rejected = True
        loan.global_manager_rejected = True
        loan.save()
    if request.user.is_sales_manager:
        loan.is_approved = False
        loan.is_rejected = True
        loan.manager_rejected = True
        loan.save()
    elif request.user.is_sales_coordinator:
        loan.is_approved = False
        loan.is_rejected = True
        loan.coordinator_rejected = True
        loan.save()
    elif request.user.is_sales_supervisor:
        loan.supervisor_approved = False
        loan.supervisor_rejected = True
        loan.save()
        
    response_data = get_response_data(
        1, redirect_url=reverse("loans:rejected_loans"), message="Rejected"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def accepted_loans(request):
    if request.user.is_superuser or request.user.is_global_manager:
        query_set = Loan.objects.filter(
            is_approved=True,
            is_rejected=False,
            is_deleted=False
        )
    elif request.user.is_sales_manager or request.user.is_sales_coordinator:
        query_set = Loan.objects.filter(
            is_deleted=False,
            is_approved=True,
            is_rejected=False,
            creator__region=request.user.region,
        )
    elif request.user.is_sales_supervisor:
        qs = Loan.objects.filter(
            is_deleted=False,
            is_approved=True,
            is_rejected=False,
        ).prefetch_related('creator')
        exe_qs = qs.filter(creator__salesexecutive__supervisor__user=request.user)
        mer_qs = qs.filter(creator__merchandiser__executive__supervisor__user=request.user)
        query_set = chain(exe_qs,mer_qs)

    context = {
        "title": "Accepted Loans",
        "instances": query_set,
    }
    return render(request, "loan/accept_loan.html", context)


@login_required
def rejected_loans(request):
    if request.user.is_superuser or request.user.is_global_manager:
        query_set = Loan.objects.filter(
            is_approved=False,
            is_rejected=True,
            is_deleted=False
        )
    elif request.user.is_sales_manager or request.user.is_sales_coordinator:
        query_set = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=True,
            creator__region=request.user.region,
        )
    elif request.user.is_sales_supervisor:
        qs = Loan.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=True,
        ).prefetch_related('creator')
        exe_qs = qs.filter(creator__salesexecutive__supervisor__user=request.user)
        mer_qs = qs.filter(creator__merchandiser__executive__supervisor__user=request.user)
        query_set = chain(exe_qs,mer_qs)

    context = {
        "title": "Rejected Loans",
        "instances": query_set,
    }
    return render(request, "loan/reject_loan.html", context)