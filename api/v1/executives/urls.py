from django.urls import path
from exicutives.models import SalesExecutive
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination

from .serializers import SalesExecutiveSerializer

app_name = "exicutives"

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
]
