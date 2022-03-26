import imp
import datetime
import json
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from core.functions import generate_form_errors, get_response_data
from .models import SalaryAdavance
# Create your views here.

@login_required
def pending_salary_advance(request):
    if request.user.is_superuser: 
        query_set = SalaryAdavance.objects.filter(
            is_approved=False,
            is_rejected=False,
            is_deleted=False,
            global_manager_approved=True
        )
    if request.user.is_global_manager: 
        query_set = SalaryAdavance.objects.filter(
            is_approved=False,
            is_rejected=False,
            is_deleted=False,
            manager_approved=True
        )
    elif request.user.is_sales_manager:
        query_set = SalaryAdavance.objects.filter(
            is_approved=False,
            is_rejected=False,
            is_deleted=False,
            coordinator_approved=True,
            user__region=request.user.region
        )
    elif request.user.is_sales_coordinator:
        query_set = SalaryAdavance.objects.filter(
            is_approved=False,
            is_rejected=False,
            is_deleted=False,
            supervisor_approved=True,
            user__region=request.user.region
        )
    elif request.user.is_sales_supervisor:
        qs = SalaryAdavance.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False,
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user)
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user)
        query_set = chain(exe_qs,mer_qs)

    context = {
        "title": "Pending Salary advance list",
        "instances": query_set,
    }
    return render(request, "salary/advance/pending_salary_advance.html", context)


@login_required
def salary_advance_single(request, pk):
    instance = get_object_or_404(SalaryAdavance, pk=pk)
    context = {
        "title": "Salary advance single page ",
        "instance": instance,
    }
    return render(request, "salary/advance/single.html", context)
    

@login_required
def accept_salary_advance(request, pk):
    salary_advance = get_object_or_404(SalaryAdavance,pk=pk)
    if request.user.is_superuser:
        salary_advance.is_approved = True
        salary_advance.is_rejected = False
        salary_advance.save()
    if request.user.is_global_manager:
        salary_advance.is_approved = True
        salary_advance.is_rejected = False
        salary_advance.global_manager_approved = True
        salary_advance.save()
    if request.user.is_sales_manager:
        salary_advance.is_approved = True
        salary_advance.is_rejected = False
        salary_advance.manager_approved = True
        salary_advance.save()
    elif request.user.is_sales_coordinator:
        salary_advance.is_approved = True
        salary_advance.is_rejected = False
        salary_advance.coordinator_approved = True
        salary_advance.save()
    elif request.user.is_sales_supervisor:
        salary_advance.supervisor_approved = True
        salary_advance.supervisor_rejected = False
        salary_advance.save()
        
    response_data = get_response_data(
        1, redirect_url=reverse("salaries:accepted_salary_advances"), message="Approved"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def reject_salary_advance(request, pk):
    salary_advance = get_object_or_404(SalaryAdavance,pk=pk)
    if request.user.is_superuser:
        salary_advance.is_approved = False
        salary_advance.is_rejected = True
        salary_advance.save()
    if request.user.is_global_manager:
        salary_advance.is_approved = False
        salary_advance.is_rejected = True
        salary_advance.global_manager_rejected =True
        salary_advance.save()
    if request.user.is_sales_manager:
        salary_advance.is_approved = False
        salary_advance.is_rejected = True
        salary_advance.manager_rejected = True
        salary_advance.save()
    elif request.user.is_sales_coordinator:
        salary_advance.is_approved = False
        salary_advance.is_rejected = True
        salary_advance.coordinator_rejected = True
        salary_advance.save()
    elif request.user.is_sales_supervisor:
        salary_advance.supervisor_approved = False
        salary_advance.supervisor_rejected = True
        salary_advance.save()

    response_data = get_response_data(
        1, redirect_url=reverse("salaries:rejected_salary_advances"), message="Rejected"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def accepted_salary_advances(request):
    if request.user.is_superuser or request.user.is_global_manager:
        query_set = SalaryAdavance.objects.filter(
            is_approved=True,
            is_rejected=False,
            is_deleted=False
        )
    elif request.user.is_sales_manager or request.user.is_sales_coordinator:
        query_set = SalaryAdavance.objects.filter(
            is_deleted=False,
            is_approved=True,
            is_rejected=False,
            user__region=request.user.region,
        )
    elif request.user.is_sales_supervisor:
        qs = SalaryAdavance.objects.filter(
            is_deleted=False,
            is_approved=True,
            is_rejected=False,
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user)
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user)
        query_set = chain(exe_qs,mer_qs)

    context = {
        "title": "Accepted Salary advances",
        "instances": query_set,
    }
    return render(request, "salary/advance/accept_salary_advance.html", context)


@login_required
def rejected_salary_advances(request):
    if request.user.is_superuser or request.user.is_global_manager:
        query_set = SalaryAdavance.objects.filter(
            is_approved=False,
            is_rejected=True,
            is_deleted=False
        )
    elif request.user.is_sales_manager or request.user.is_sales_coordinator:
        query_set = SalaryAdavance.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=True,
            user__region=request.user.region,
        )
    elif request.user.is_sales_supervisor:
        qs = SalaryAdavance.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=True,
        ).prefetch_related('user')
        exe_qs = qs.filter(user__salesexecutive__supervisor__user=request.user)
        mer_qs = qs.filter(user__merchandiser__executive__supervisor__user=request.user)
        query_set = chain(exe_qs,mer_qs)

    context = {
        "title": "Rejected Salary advances",
        "instances": query_set,
    }
    return render(request, "salary/advance/reject_salary_advance.html", context)


