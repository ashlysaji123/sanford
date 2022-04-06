from rest_framework import serializers

from core.models import SubRegion, Language, Region, Area, Year,LocalArea,Shop


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ("pk", "name")


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("pk", "family", "name", "native_name", "lang_code")

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("pk", "location", "name", "contact_number", "contact_number2","area","local_area")


class SubRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRegion
        fields = ("pk", "name", "slug", "sub_region_code")


class AreaSerializer(serializers.ModelSerializer):
    sub_region_name = serializers.ReadOnlyField()

    class Meta:
        model = Area
        fields = (
            "pk",
            "name",
            "type",
            "sub_region",
            "sub_region_name",
            "slug",
            "area_code",
            "tin_number",
        )

class LocalAreaSerializer(serializers.ModelSerializer):
    area_name = serializers.ReadOnlyField()

    class Meta:
        model = LocalArea
        fields = (
            "pk",
            "name",
            "area",
            "area_name",
            "slug",
            "local_area_code",
            "tin_number",
        )


class RegionSerializer(serializers.ModelSerializer):
    area_name = serializers.ReadOnlyField()

    class Meta:
        model = Region
        fields = ("pk", "name", "area_name")
