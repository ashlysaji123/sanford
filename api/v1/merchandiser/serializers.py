from rest_framework import serializers

from merchandiser.models import Merchandiser, MerchandiserTarget, MerchandiserTask


class MerchandiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandiser
        fields = "__all__"


class MerchandiserTargetSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField()

    class Meta:
        model = MerchandiserTarget
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


class MerchandiserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchandiserTask
        fields = ("id", "task", "is_completed")


class MerchandiserProfileSerializer(serializers.ModelSerializer):
    region = serializers.SerializerMethodField()
    sub_region = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    shop = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()

    class Meta:
        model = Merchandiser
        fields = "__all__"

    def get_region(self, obj):
        return obj.area.sub_region.region.name

    def get_shop(self, obj):
        return obj.shop.name

    def get_sub_region(self, obj):
        return obj.area.sub_region.name

    def get_area(self, obj):
        return obj.area.name
