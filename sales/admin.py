from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from core.actions import mark_active, mark_deleted

from .models import OpeningStock, Sales,SaleItems

admin.site.register(Sales)
admin.site.register(SaleItems)

# @admin.register(Target)
# class TargetAdmin(ImportExportActionModelAdmin):
#     list_display = ["__str__", "year","month","amount", "is_deleted"]
#     list_filter = ["is_deleted","user", "month",]
#     actions = [mark_deleted, mark_active]


# @admin.register(OpeningStock)
# class OpeningStockAdmin(ImportExportActionModelAdmin):
#     list_display = ["merchandiser", "product", "count", "is_deleted"]
#     list_filter = ["is_deleted"]
#     autocomplete_fields = ('product','merchandiser')
#     actions = [mark_deleted, mark_active]

admin.site.register(
    OpeningStock
)