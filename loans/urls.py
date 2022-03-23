from django.urls import path

from . import views

app_name = "loans"

urlpatterns = [
    path("loan/requests", views.pending_loan_requests, name="pending_loan_requests"),
    path("loan/single/<str:pk>/", views.loan_single, name="loan_single"),
    path("accept/loan/<str:pk>/", views.accept_loan, name="accept_loan"),
    path("reject/loan/<str:pk>/", views.reject_loan, name="reject_loan"),
    path("accepted/loans", views.accepted_loans, name="accepted_loans"),
    path("rejected/loans", views.rejected_loans, name="rejected_loans"),
]
