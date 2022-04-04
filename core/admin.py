from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from core.actions import mark_active, mark_deleted

from .models import BlockedIP, SubRegion, Language, Region, Shop, Area,LocalArea, Year,UserLog


@admin.register(UserLog)
class UserLogAdmin(ImportExportActionModelAdmin):
    list_display = ["title", "description"]


@admin.register(Year)
class YearAdmin(ImportExportActionModelAdmin):
    list_display = ["name", "is_deleted"]
    list_filter = ["is_deleted"]
    actions = [mark_deleted, mark_active]


@admin.register(Language)
class LanguageAdmin(ImportExportActionModelAdmin):
    list_display = ["name", "family", "native_name", "lang_code", "is_deleted"]
    list_filter = ["is_deleted"]
    search_fields = ["name"]
    actions = [mark_deleted, mark_active]


@admin.register(SubRegion)
class SubRegionAdmin(ImportExportActionModelAdmin):
    list_display = ["name", "is_deleted","sub_region_type","region"]
    list_filter = ["is_deleted","sub_region_type"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    actions = [mark_deleted, mark_active]


@admin.register(Area)
class AreaAdmin(ImportExportActionModelAdmin):
    list_display = ["name", "area_code", "sub_region","is_deleted"]
    list_filter = ["sub_region","is_deleted"]
    search_fields = ["name"]
    autocomplete_fields = ["sub_region"]
    actions = [mark_deleted, mark_active]

@admin.register(LocalArea)
class LocalAreaAdmin(ImportExportActionModelAdmin):
    list_display = ["name", "local_area_code", "area", "is_deleted"]
    list_filter = ["area", "is_deleted"]
    search_fields = ["name"]
    autocomplete_fields = ["area"]
    actions = [mark_deleted, mark_active]


@admin.register(Region)
class RegionAdmin(ImportExportActionModelAdmin):
    list_display = ["name", "is_deleted"]
    list_filter = ["is_deleted"]
    search_fields = ["name"]
    actions = [mark_deleted, mark_active]


@admin.register(BlockedIP)
class BlockedIPAdmin(ImportExportActionModelAdmin):
    list_display = ["ip_address", "is_deleted"]
    search_fields = ["ip_address"]
    actions = [mark_deleted, mark_active]


admin.site.register(Shop)
