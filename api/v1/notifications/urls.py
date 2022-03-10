from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination
from notifications.models import Notification

from .serializers import NotificationSerializer

app_name = "notification"

urlpatterns = [
    path(
        "",
        ListAPIView.as_view(
            queryset=Notification.objects.filter(is_deleted=False),
            serializer_class=NotificationSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Notification.objects.filter(is_deleted=False),
            serializer_class=NotificationSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
]
