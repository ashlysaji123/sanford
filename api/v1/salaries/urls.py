from django.urls import path

from . import views

app_name = "salaries"

urlpatterns = [
    path("request-for/salary-advance/", views.create_salary_advance_request),
    path("my-salary-advance/requests/", views.my_salary_advance_requests),
    path("salary/advance/list/", views.salary_advance_list),  
]