from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.pagination import StandardResultsSetPagination
from leave.models import LeaveRequest

from . import views
from .serializers import LeaveRequestSerializer

app_name = "leave"

urlpatterns = [
    path(
        "",
        ListAPIView.as_view(
            queryset=LeaveRequest.objects.filter(is_deleted=False),
            serializer_class=LeaveRequestSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=LeaveRequest.objects.filter(is_deleted=False),
            serializer_class=LeaveRequestSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path("myreport/", views.LeaveRequestSummaryView.as_view()),
    path("add-leave/", views.create_leave),
    path("my-leave-report/", views.my_leave_reports),
]
