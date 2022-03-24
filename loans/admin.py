from django.contrib import admin

from loans.models import Loan

# Register your models here.
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['amount','reason', 'guarantee', 'approved_date', 'is_approved', 'is_rejected', 'duration']

