from rest_framework import serializers

from coordinators.models import (
    SalesCoordinator, 
    SalesCoordinatorTarget, 
    SalesCoordinatorTask,
    SalesManager
)


class SalesCoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesCoordinator
        fields = "__all__"


class SalesManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesManager
        fields = "__all__"

class SalesCoordinatorTargetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesCoordinatorTarget
        fields = (
            "id",
            "year",
            "month",
            "target_amount",
            "current_amount",
            "target_type",
            "is_completed",
        )

class SalesCoordinatorTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesCoordinatorTask
        fields = ("id", "task", "is_completed")


class SalesCoordinatorProfileSerializer(serializers.ModelSerializer):
    region = serializers.SerializerMethodField()

    class Meta:
        model = SalesCoordinator
        fields = "__all__" 

    def get_region(self, obj):
        return obj.region.name
