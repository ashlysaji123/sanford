from django.contrib import admin

from .models import Staff,StaffHistoryLog
# Register your models here.

admin.site.register(Staff)
admin.site.register(StaffHistoryLog)