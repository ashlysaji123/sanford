from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField()

    class Meta:
        model = Notification
        fields = ("pk", "title", "description", "created", "updated", "created_at")
