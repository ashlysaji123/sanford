from rest_framework import serializers

from expenses.models import Expenses


class CreateExpensesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expenses
        fields = ("date", "expense_type", "amount","description")


class ExpensesListSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()

    class Meta:
        model = Expenses
        fields = ("date", "pk", "expense_type", "amount", "description", "is_approved", "is_rejected", "user", "first_name")

    def get_first_name(self,obj):
        return obj.user.first_name
        