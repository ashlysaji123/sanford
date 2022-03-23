from rest_framework import serializers

from salaries.models import SalaryAdavance


class CreateSalaryAdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryAdavance
        fields = ('amount', 'description')

class SalaryAdvanceListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()

    class Meta:
        model = SalaryAdavance
        fields = ('id','user','username','first_name','amount', 'approved_date','description', 'is_approved', 'is_rejected')

    def get_username(self,obj):
        if obj.user:
            return obj.user.username

    def get_first_name(self,obj):
        if obj.user:
            return obj.user.first_name
