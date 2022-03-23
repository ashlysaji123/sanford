import imp
import datetime
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from core.functions import generate_form_errors, get_response_data
from .models import Loan
# Create your views here.

@login_required
def pending_loan_requests(request):
    if request.user.is_superuser:
        query_set = Loan.objects.filter(
            is_approved=False,
            is_rejected=False,
            manager_approved=True,
            is_deleted=False
        )
    elif request.user.is_sales_manager:
        query_set = Loan.objects.filter(
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            is_deleted=False,
            creator__region=request.user.region
        )
    elif request.user.is_sales_coordinator:
        query_set = Loan.objects.filter(
            is_approved=False,
            is_rejected=False,
            executive_approved=True,
            is_deleted=False,
            creator__region=request.user.region
        )
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
    elif request.user.is_sales_manager:
        loan.manager_approved = True
        loan.manager_rejected = False
        loan.save()
    elif request.user.is_sales_coordinator:
        loan.coordinator_approved = True
        loan.coordinator_rejected = False
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
        loan.is_rejected=True
        loan.is_approved=False
        loan.save()
    elif request.user.is_sales_manager:
        loan.manager_rejected = True
        loan.manager_approved = False
        loan.save()
    elif request.user.is_sales_coordinator:
        loan.coordinator_rejected = True
        loan.coordinator_approved = False
        loan.save()
        
    response_data = get_response_data(
        1, redirect_url=reverse("loans:rejected_loans"), message="Rejected"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def accepted_loans(request):
    if request.user.is_superuser:
        query_set = Loan.objects.filter(
            is_approved=True,
            is_rejected=False,
            is_deleted=False
        )
    else:
        query_set = Loan.objects.filter(
            is_approved=True,
            is_rejected=False,
            is_deleted=False,
            creator__region=request.user.region
        )
    context = {
        "title": "Accepted Loans",
        "instances": query_set,
    }
    return render(request, "loan/accept_loan.html", context)


@login_required
def rejected_loans(request):
    if request.user.is_superuser:
        query_set = Loan.objects.filter(
            is_approved=False,
            is_rejected=True,
            is_deleted=False
        )
    else:
        query_set = Loan.objects.filter(
            is_approved=False,
            is_rejected=True,
            is_deleted=False,
            creator__region=request.user.region
        )
    context = {
        "title": "Rejected Loans",
        "instances": query_set,
    }
    return render(request, "loan/reject_loan.html", context)