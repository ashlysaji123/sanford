from rest_framework import serializers

from coordinators.models import SalesCoordinator, SalesManager


class SalesCoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesCoordinator
        fields = "__all__"


class SalesManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesManager
        fields = "__all__"
