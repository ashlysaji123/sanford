from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination
from rewards.models import RewardPoint

from . import views
from .serializers import RewardPointSerializer

app_name = "rewards"

urlpatterns = [
    path(
        "",
        ListAPIView.as_view(
            queryset=RewardPoint.objects.filter(is_deleted=False),
            serializer_class=RewardPointSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path(
        "view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=RewardPoint.objects.filter(is_deleted=False),
            serializer_class=RewardPointSerializer,
            permission_classes =[IsAuthenticated],
        ),
    ),
    path("myreport/", views.RewardSummaryView.as_view()),
]
