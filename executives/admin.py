from django.contrib import admin

from .models import SalesExecutive, SalesExecutiveTarget, SalesExecutiveTask

admin.site.register(SalesExecutive)
admin.site.register(SalesExecutiveTarget)
admin.site.register(SalesExecutiveTask)

# @admin.register(SalesExicutive)
# class SalesExicutiveAdmin(ImportExportActionModelAdmin):
#     list_display = ["__str__","user", "check_in","check_out", "is_deleted","location","late_reason","is_leave"]
#     list_filter = ["check_in","is_deleted"]
#     actions = [mark_deleted, mark_active]


# @admin.register(SalesExicutiveTarget)
# class SalesExicutiveTargetAdmin(ImportExportActionModelAdmin):
#     list_display = ["__str__","user", "start_date","end_date", "is_deleted","leave_reason","is_approved","is_rejected"]
#     list_filter = ["check_in","is_deleted"]
#     actions = [mark_deleted, mark_active]
