from rest_framework import serializers

from loans.models import Loan,LoanLog


class CreateLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('amount', 'reason', 'duration', 'guarntee')

class LoanListSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = ('id','first_name','amount', 'reason', 'approved_date','duration', 'is_approved', 'is_rejected','guarntee','paid_amount','is_returned_completely')


    def get_first_name(self,obj):
        if obj.guarantee:
            return obj.guarantee.first_name


class CreateLoanLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanLog
        fields = ('date', 'carrier', 'amount')

class LoanLogListSerializer(serializers.ModelSerializer):
    # first_name = serializers.SerializerMethodField()

    class Meta:
        model = LoanLog
        fields = ('id','date','carrier', 'amount', 'created','loan')


    # def get_first_name(self,obj):
    #     if obj.guarntee:
    #         return obj.guarntee.first_name

