import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.attendance.utils import get_daily_attendance_sum
from attendance.models import Attendance
from django.conf import settings
from .serializers import AttendanceSerializer, MarkAttendanceSerializer


class MarkAttendanceIn(APIView):
    """
    * mark Check in of current user
    * Method: POST Only
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = MarkAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            today = datetime.date.today()
            check_in = serializer.validated_data["check_in_time"]

            if check_in > settings.SANFORDCORP_ENTRY_TIME:
                serializer.save(user=user, creator=user,is_late=True,date=today)
                response_data = {"status": True, "data": serializer.data}
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                serializer.save(user=user, creator=user,date=today)
                response_data = {"status": True, "data": serializer.data}
                return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def MarkAttendanceOut(request, pk):
    """
    * mark Check-out of current user
    * Method: POST Only
    """
    attandance = Attendance.objects.get(user=request.user, pk=pk)
    serializer = MarkAttendanceSerializer(
        attandance, data=request.data, context={"request": request}, partial=True
    )
    if serializer.is_valid():
        # Calculating daily worked hours of current user
        check_in = attandance.check_in_time
        check_out = serializer.validated_data["check_out_time"]
        working_hours = (check_in - check_out).seconds / (60 * 60)
        serializer.save(working_hours=working_hours)
        response_data = {"status": True, "data": serializer.data}
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def MyAttandanceSummaryView(request):
    user = request.user
    attandance = DailyAttendance.objects.filter(user=user)
    serializer = DailyAttendanceSerializer(attandance, context={"request": request}, many=True)
    response_data = {"status": "true", "attendance": serializer.data}
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def old_MyAttandanceSummaryView(request):
    """
    View to list all Attendace of current user
    """
    user = request.user
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    # Weekly attandance Query result.
    queryset = Attendance.objects.filter(
        user=request.user,
        is_deleted=False,
        check_in_time__range=[start_week, end_week],
        is_leave=False,
    )

    query = request.GET.get("q")

    """ Listing attendance by filtering parameeters"""
    if query == "monthly":
        month = date.month
        queryset = Attendance.objects.filter(
            user=request.user,
            is_deleted=False,
            check_in_time__month=month,
            is_leave=False,
        )
    if query == "alltime":
        queryset = Attendance.objects.filter(
            user=request.user, is_deleted=False, is_leave=False
        )
    # Daily query sum
    dic = get_daily_attendance_sum(queryset)

    serializer = AttendanceSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )

    response_data = {"status": "true", "attendance": serializer.data, "data": dic}

    return Response(response_data, status=status.HTTP_201_CREATED)
