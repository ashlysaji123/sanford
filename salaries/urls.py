from django.urls import path

from . import views

app_name = "salaries"

urlpatterns = [
    path("pending/salary/advance", views.pending_salary_advance, name="pending_salary_advance"),
    path("salary/advance/single/<str:pk>/", views.salary_advance_single, name="salary_advance_single"),
    path("accept/salary/advance/<str:pk>/", views.accept_salary_advance, name="accept_salary_advance"),
    path("reject/salary/advance/<str:pk>/", views.reject_salary_advance, name="reject_salary_advance"),
    path("accepted/salary/advance", views.accepted_salary_advances, name="accepted_salary_advances"),
    path("rejected/salary/advance", views.rejected_salary_advances, name="rejected_salary_advances"),
]
