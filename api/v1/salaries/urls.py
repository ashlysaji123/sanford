from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination

from . import views

app_name = "documents"

urlpatterns = [
    path("create-documents/", views.create_documents),
    path("update-documents/<str:pk>/", views.update_document),
    path("my-documents/<str:pk>/", views.my_documents),
]
