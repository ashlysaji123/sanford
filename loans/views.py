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
def pending_loan(request):
    query_set = Loan.objects.filter(
        is_approved=False,
        is_rejected=False,
    )
    context = {
        "title": "Pending Loan",
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
def accept_loan(request):
    query_set = Loan.objects.filter(
        is_approved=True,
        is_rejected=False,
    )
    context = {
        "title": "Accept Loan",
        "instances": query_set,
    }
    return render(request, "loan/accept_loan.html", context)