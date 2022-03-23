from django.urls import path

from . import views

app_name = "loans"

urlpatterns = [
    path("request-for/loan", views.create_loan_request),
    path("my-loan/requests", views.my_loan_requests),
    path("loan/requests", views.loan_requests),
]