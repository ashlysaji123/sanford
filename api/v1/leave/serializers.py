from rest_framework import serializers

from leave.models import LeaveRequest


class LeaveRequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = (
            "pk",
            "user",
            "startdate",
            "enddate",
            "leavetype",
            "reason",
            "is_rejected",
            "is_approved",
            "total_available_leave",
            "leave_duration",
        )


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = (
            "pk",
            "user",
            "startdate",
            "enddate",
            "leavetype",
            "reason",
            "is_approved",
            "total_available_leave",
            "leave_duration",
        )
