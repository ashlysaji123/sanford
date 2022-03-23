from django.urls import path

from . import views

app_name = "loans"

urlpatterns = [
    path("pending/loan", views.pending_loan, name="pending_loan"),
    path("loan/single/<str:pk>/", views.loan_single, name="loan_single"),
    path("accept/loan", views.accept_loan, name="accept_loan"),
    path("reject/loan", views.reject_loan, name="reject_loan"),
]
