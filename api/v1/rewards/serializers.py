from rest_framework import serializers

from rewards.models import RewardPoint


class RewardPointSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.fullname")

    class Meta:
        model = RewardPoint
        fields = (
            "pk",
            "user",
            "user_name",
            "year",
            "month",
            "point",
            "status",
            "description",
        )
