from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from core.actions import mark_active, mark_deleted

from .models import RewardPoint


@admin.register(RewardPoint)
class RewardPointAdmin(ImportExportActionModelAdmin):
    list_display = ["__str__", "user", "year", "month", "point", "status", "is_deleted"]
    list_filter = ["status", "is_deleted"]
    actions = [mark_deleted, mark_active]
