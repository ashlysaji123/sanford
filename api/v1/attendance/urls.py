from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from attendance.models import Attendance
from core.pagination import StandardResultsSetPagination

from . import views
from .serializers import AttendanceSerializer

app_name = "attendance"

urlpatterns = [
    path(
        "",
        ListAPIView.as_view(
            queryset=Attendance.objects.filter(is_deleted=False),
            serializer_class=AttendanceSerializer,
            pagination_class=StandardResultsSetPagination,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path(
        "view/<str:pk>/",
        RetrieveAPIView.as_view(
            queryset=Attendance.objects.filter(is_deleted=False),
            serializer_class=AttendanceSerializer,
            permission_classes=[IsAuthenticated],
        ),
    ),
    path("mark-check-in/", views.MarkAttendanceIn.as_view(), name="mark_in_attendance"),
    path(
        "mark-check-out/<str:pk>/", views.MarkAttendanceOut, name="mark_out_attendance"
    ),
    path("my-attandance/", views.MyAttandanceSummaryView, name="my_attendance"),
]
