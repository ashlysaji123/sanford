from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from core.actions import mark_active, mark_deleted

from .models import LeaveRequest,LeaveApproval


@admin.register(LeaveRequest)
class LeaveRequestAdmin(ImportExportActionModelAdmin):
    list_display = [
        "__str__",
        "startdate",
        "enddate",
        "leavetype",
        "is_approved",
        "is_deleted",
    ]
    list_filter = ["startdate", "enddate", "leavetype", "is_approved", "is_deleted"]
    actions = [mark_deleted, mark_active]


admin.site.register(LeaveApproval)