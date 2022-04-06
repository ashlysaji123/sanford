from django.urls import path

from . import views

app_name = "loans"

urlpatterns = [
    path("request-for/loan", views.create_loan_request),
    path("my-loan/requests", views.my_loan_requests),
    path("loan/requests", views.loan_requests),
    # loan logs
    path("add-loan-payment/<str:pk>/", views.create_loan_payments),
    path("my-loan-logs/<str:pk>/", views.my_loan_logs),
    path("loan-log/single/<str:pk>/", views.loan_log_single),
]