from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination
from api.v1.accounts.serializers import UserSerializer
from accounts.models import User
from coordinators.models import SalesCoordinator,SalesManager
from .serializers import SalesManagerSerializer,SalesCoordinatorSerializer

app_name = "coordinators"

urlpatterns = [
    path(
        "managers",
        ListAPIView.as_view(
            queryset=SalesManager.objects.filter(is_deleted=False),
            serializer_class=SalesManagerSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "manager/single/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=SalesManager.objects.filter(is_deleted=False),
            serializer_class=SalesManagerSerializer,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "coordinators",
        ListAPIView.as_view(
            queryset=SalesCoordinator.objects.filter(is_deleted=False),
            serializer_class=SalesCoordinatorSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "coordinator/single/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=SalesCoordinator.objects.filter(is_deleted=False),
            serializer_class=SalesCoordinatorSerializer,
            permission_classes =[IsAuthenticated],
        ),
    ),
]
