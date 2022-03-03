from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from core.actions import mark_active, mark_deleted

from .models import SalesManager,SalesManagerTarget,SalesCoordinator,SalesCoordinatorTarget,SalesCoordinatorTask,SalesManagerTask




admin.site.register(SalesManager)
admin.site.register(SalesManagerTarget)
admin.site.register(SalesCoordinator)
admin.site.register(SalesCoordinatorTarget)
admin.site.register(SalesCoordinatorTask)
admin.site.register(SalesManagerTask)

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
