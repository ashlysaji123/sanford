from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path("claim-requests", views.pending_claim_requests, name="pending_claim_requests"),
    path(
        "approved-expenses", views.approved_expense_list, name="approved_expense_list"
    ),
    path(
        "approve-claim/<str:pk>/",
        views.approve_claim_request,
        name="approve_claim_request",
    ),
    path(
        "reject-claim/<str:pk>/",
        views.reject_claim_request,
        name="reject_claim_request",
    ),
    path(
        "single-expense-claim/<str:pk>/",
        views.expense_claim_single,
        name="expense_claim_single",
    ),
]
