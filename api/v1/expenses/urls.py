from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination

from . import views

app_name = "expenses"

urlpatterns = [
    path("create-expenses/", views.create_expenses),
    path("my_expenses/", views.my_expenses),
    path("delete_expenses/<str:pk>/", views.delete_expenses),
]
