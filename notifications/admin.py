from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from core.actions import mark_active, mark_deleted

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(ImportExportActionModelAdmin):
    list_display = ["title", "is_deleted"]
    list_filter = ["is_deleted"]
    actions = [mark_deleted, mark_active]
