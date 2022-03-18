from django.urls import path
from executives.models import SalesExecutive
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination

from . import views
from .serializers import SalesExecutiveSerializer

app_name = "executives"

urlpatterns = [
    path(
        "",
        ListAPIView.as_view(
            queryset=SalesExecutive.objects.filter(is_deleted=False),
            serializer_class=SalesExecutiveSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=SalesExecutive.objects.filter(is_deleted=False),
            serializer_class=SalesExecutiveSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path("salesexecutive/target/", views.salesexecutive_target),
    path("salesexecutive/task/", views.salesexecutive_task),
    path("salesexecutive/completed/task/", views.salesexecutive_completed_task),
    path("salesexecutive/mark/task/<str:pk>/", views.salesexecutive_mark_task),
    path("salesexecutive/profile/",views.salesexecutive_profile),
]
