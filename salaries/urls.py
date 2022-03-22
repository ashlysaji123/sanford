from django.urls import path

from . import views

app_name = "salaries"

urlpatterns = [
    path("pending/salary/advance", views.pending_salary_advance, name="pending_salary_advance"),
    path("salary/advance/single/<str:pk>/", views.salary_advance_single, name="salary_advance_single"),
    path("accept/salary/advance", views.accept_salary_advance, name="accept_salary_advance"),
]
