from rest_framework import serializers

from executives.models import SalesExecutive


class SalesExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesExecutive
        fields = "__all__"
