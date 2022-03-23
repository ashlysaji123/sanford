import imp
import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from core.functions import generate_form_errors, get_response_data



from .models import SalaryAdavance
# Create your views here.

@login_required
def pending_salary_advance(request):
    query_set = SalaryAdavance.objects.filter(
        is_approved=False,
        is_rejected=False,
    )
    context = {
        "title": "Pending Salaries",
        "instances": query_set,
    }
    return render(request, "salary/advance/pending_salary_advance.html", context)


@login_required
def salary_advance_single(request, pk):
    instance = get_object_or_404(SalaryAdavance, pk=pk)
    context = {
        "title": "Salary single page ",
        "instance": instance,
    }
    return render(request, "salary/advance/single.html", context)
    

@login_required
def accept_salary_advance(request):
    query_set = SalaryAdavance.objects.filter(
        is_approved=True,
        is_rejected=False,
    )
    context = {
        "title": "Accept Salaries",
        "instances": query_set,
    }
    return render(request, "salary/advance/accept_salary_advance.html", context)


@login_required
def reject_salary_advance(request):
    query_set = SalaryAdavance.objects.filter(
        is_approved=False,
        is_rejected=True,
    )
    context = {
        "title": "Reject Salaries",
        "instances": query_set,
    }
    return render(request, "salary/advance/reject_salary_advance.html", context)


