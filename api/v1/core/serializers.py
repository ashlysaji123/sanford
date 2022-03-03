from rest_framework import serializers

from core.models import Country, Language, Region, State, Year


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ("pk", "name")


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("pk", "family", "name", "native_name", "lang_code")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("pk", "name", "slug", "country_code")


class StateSerializer(serializers.ModelSerializer):
    country_name = serializers.ReadOnlyField()

    class Meta:
        model = State
        fields = ( "pk", "name", "type", "country", "country_name", "slug", "state_code", "tin_number",)


class RegionSerializer(serializers.ModelSerializer):
    state_name = serializers.ReadOnlyField()

    class Meta:
        model = Region
        fields = ("pk", "name", "state_name")
