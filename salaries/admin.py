from django.contrib import admin


from salaries.models import SalaryAdavance

# Register your models here.
@admin.register(SalaryAdavance)
class SalaryadvanceAdmin(admin.ModelAdmin):
    list_display = ['amount', 'description', 'user', 'approved_date', 'is_approved', 'is_rejected']