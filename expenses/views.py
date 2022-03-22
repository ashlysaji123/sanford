import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.functions import get_response_data

from .models import Expenses


@login_required
def pending_claim_requests(request):
    if request.user.is_superuser:
        query_set = Expenses.objects.filter(
            is_deleted=False, is_approved=False, is_rejected=False,manager_approved=True
        )
    elif request.user.is_sales_manager:
        query_set = Expenses.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            coordinator_approved=True,
            user__region=request.user.region,
        )
    elif request.user.is_sales_coordinator:
        query_set = Expenses.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            executive_approved=True,
            user__region=request.user.region,
        )

    context = {
        "title": "Pending Expense Claims",
        "instances": query_set,
    }
    return render(request, "expenses/pending/list.html", context)


@login_required
def approved_expense_list(request):
    if request.user.is_superuser:
        query_set = Expenses.objects.filter(
            is_deleted=False, is_approved=True, is_rejected=False
        )
    else:
        query_set = Expenses.objects.filter(
            is_deleted=False,
            is_approved=True,
            is_rejected=False,
            user__region=request.user.region,
        )

    context = {
        "title": "Approved Expenses",
        "instances": query_set,
    }
    return render(request, "expenses/approved/list.html", context)


def approve_claim_request(request, pk):
    expense = get_object_or_404(Expenses,pk=pk)
    if request.user.is_superuser:
        expense.is_approved = True
        expense.is_rejected = False
        expense.save()
    elif request.user.is_sales_manager:
        expense.manager_approved = True
        expense.manager_rejected = False
        expense.save()
    elif request.user.is_sales_coordinator:
        expense.coordinator_approved = True
        expense.coordinator_rejected = False
        expense.save()

    response_data = get_response_data(
        1, redirect_url=reverse("expenses:approved_expense_list"), message="Approved"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


def reject_claim_request(request, pk):
    expense = get_object_or_404(Expenses,pk=pk)
    if request.user.is_superuser:
        expense.is_rejected=True
        expense.is_approved=False
        expense.save()
    elif request.user.is_sales_manager:
        expense.manager_rejected = True
        expense.manager_approved = False
        expense.save()
    elif request.user.is_sales_coordinator:
        expense.coordinator_rejected = True
        expense.coordinator_approved = False
        expense.save()
        
    response_data = get_response_data(
        1, redirect_url=reverse("expenses:pending_claim_requests"), message="Rejected"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


@login_required
def expense_claim_single(request, pk):
    instance = get_object_or_404(Expenses, pk=pk)
    context = {"title": "Expense Claim ", "instance": instance}
    return render(request, "expenses/single.html", context)
