from rest_framework import serializers

from attendance.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ("pk", "user", "check_in_time", "check_out_time", "location", "late_reason","is_leave","working_hours")


class MarkAttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ("pk","check_in_time","check_out_time", "location", "late_reason","working_hours")
