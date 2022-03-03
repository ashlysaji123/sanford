from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from core.actions import mark_active, mark_deleted

from .models import BlockedIP, Country, Language, Region, State, Year,Shop


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


@admin.register(Country)
class CountryAdmin(ImportExportActionModelAdmin):
    list_display = ["name", "is_deleted"]
    list_filter = ["is_deleted"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    actions = [mark_deleted, mark_active]


@admin.register(State)
class StateAdmin(ImportExportActionModelAdmin):
    list_display = ["name", "state_code", "tin_number", "country", "type", "is_deleted"]
    list_filter = ["country", "type", "is_deleted"]
    search_fields = ["name"]
    autocomplete_fields = ["country"]
    prepopulated_fields = {"slug": ("name",)}
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