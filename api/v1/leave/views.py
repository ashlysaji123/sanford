import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from leave.models import LeaveRequest

from .serializers import LeaveRequestListSerializer, LeaveRequestSerializer


class LeaveRequestSummaryView(ListAPIView):
    """
    View to list all Leave Request assigned with current user
    """

    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LeaveRequest.objects.filter(user=self.request.user, is_deleted=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_leave(request):
    serializer = LeaveRequestSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        user = request.user
        """
        Taking startdate and and enddate and
        calculating days of taken leave
        """
        startdate = serializer.validated_data["startdate"]
        enddate = serializer.validated_data["enddate"]
        if startdate > enddate:
            return Response(
                {"message": "Please Check the dates!."}, status=status.HTTP_200_OK
            )
        date_format = "%Y-%M-%d"
        a = datetime.datetime.strptime(str(startdate), date_format)
        b = datetime.datetime.strptime(str(enddate), date_format)
        delta = b - a
        leave_days = delta.days + 1
        serializer.save(
            creator=user, 
            user=user, 
            leave_duration=leave_days,
        )
        response = {"message": "Leave requested successfully.\n waite for the approvals.!"}
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {"status": 400, "message": serializer.errors}
        return Response(response, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_leave_reports(request):
    queryset = LeaveRequest.objects.filter(
        is_deleted=False, user=request.user
    ).order_by("-created")

    leave_query = LeaveRequest.objects.filter(
        is_deleted=False, user=request.user, is_approved=True
    )
    total_leave_taken = 0
    for i in leave_query:
        total_leave_taken += i.leave_duration
    serializer = LeaveRequestListSerializer(
        queryset, context={"request": request}, many=True, read_only=True
    )
    response = {
        "status": 200,
        "data": serializer.data,
        "leave_taken": total_leave_taken,
    }

    return Response(response, status=status.HTTP_200_OK)
