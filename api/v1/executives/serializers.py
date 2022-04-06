from rest_framework import serializers

from executives.models import SalesExecutive ,SalesExecutiveTarget, SalesExecutiveTask


class SalesExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesExecutive
        fields = "__all__"


class SalesExecutiveTargetSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField()
        
    class Meta:
        model = SalesExecutiveTarget
        fields = (
            "id",
            "year",
            "month",
            "target_amount",
            "current_amount",
            "target_type",
            "is_completed",
            "percentage",
        )

    def get_percentage(self, obj):
        target_amount = obj.target_amount
        current_amount = obj.current_amount
        return (current_amount / target_amount) * 100

class SalesExecutiveTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesExecutiveTask
        fields = ("id", "task", "is_completed")

class SalesExecutiveProfileSerializer(serializers.ModelSerializer):
    region = serializers.SerializerMethodField()
    
    class Meta:
        model = SalesExecutive
        fields = "__all__"

    def get_region(self, obj):
        return obj.region.name

    
