import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.functions import get_response_data

from .models import Expenses


@login_required
def pending_claim_requests(request):
    if request.user.is_sales_manager:
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
            supervisor_approved=True,
            user__region=request.user.region,
        )
    elif request.user.is_sales_supervisor:
        query_set = Expenses.objects.filter(
            is_deleted=False,
            is_approved=False,
            is_rejected=False,
            supervisor_approved=False,
            supervisor_rejected=False,
            user__salesexecutive__supervisor__user=request.user
        )

    context = {
        "title": "Pending Expense Claims",
        "instances": query_set,
    }
    return render(request, "expenses/pending/list.html", context)


@login_required
def approved_expense_list(request):
    if request.user.is_superuser or request.user.is_global_manager:
        query_set = Expenses.objects.filter(
            is_deleted=False, is_approved=True, is_rejected=False
        )
    elif request.user.is_sales_manager or request.user.is_sales_coordinator:
        query_set = Expenses.objects.filter(
            is_deleted=False,
            is_approved=True,
            is_rejected=False,
            user__region=request.user.region,
        )
    elif request.user.is_sales_supervisor:
        query_set = Expenses.objects.filter(
            is_deleted=False,
            is_approved=True,
            is_rejected=False,
            user__salesexecutive__supervisor__user=request.user
        )

    context = {
        "title": "Approved Expenses",
        "instances": query_set,
    }
    return render(request, "expenses/approved/list.html", context)


def approve_claim_request(request, pk):
    expense = get_object_or_404(Expenses,pk=pk)
    if request.user.is_sales_manager:
        expense.is_approved = True
        expense.is_rejected = False
        expense.save()
    elif request.user.is_sales_coordinator:
        expense.is_approved = True
        expense.is_rejected = False
        expense.coordinator_approved = True
        expense.save()
    elif request.user.is_sales_supervisor:
        expense.supervisor_approved = True
        expense.supervisor_rejected = False
        expense.save()

    response_data = get_response_data(
        1, redirect_url=reverse("expenses:approved_expense_list"), message="Approved"
    )
    return HttpResponse(
        json.dumps(response_data), content_type="application/javascript"
    )


def reject_claim_request(request, pk):
    expense = get_object_or_404(Expenses,pk=pk)
    if request.user.is_sales_manager:
        expense.is_rejected = True
        expense.is_approved = False
        expense.save()
    elif request.user.is_sales_coordinator:
        expense.is_rejected = True
        expense.is_approved = False
        expense.coordinator_rejected = True
        expense.save()
    elif request.user.is_sales_supervisor:
        expense.supervisor_approved = False
        expense.supervisor_rejected = True
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
