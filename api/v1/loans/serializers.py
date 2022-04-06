from rest_framework import serializers

from loans.models import Loan


class CreateLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('amount', 'reason', 'duration', 'guarntee')

class LoanListSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = ('id','first_name','amount', 'reason', 'approved_date','duration', 'is_approved', 'is_rejected','guarantee')


    def get_first_name(self,obj):
        if obj.guarantee:
            return obj.guarantee.first_name

