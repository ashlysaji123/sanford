from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from core.actions import mark_active, mark_deleted

from .models import Category, Product, ProductWishList, SubCategory


@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin):
    actions = [mark_deleted, mark_active]
    list_display = ["name", "code", "creator", "is_deleted"]
    list_filter = ["is_deleted"]
    search_fields = ["name"]
    autocomplete_fields = ["creator"]


@admin.register(SubCategory)
class SubCategoryAdmin(ImportExportActionModelAdmin):
    actions = [mark_deleted, mark_active]
    list_display = ["name", "category", "code", "creator", "is_deleted"]
    autocomplete_fields = ["creator"]
    list_filter = ["category", "is_deleted"]
    search_fields = ["name"]




@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    actions = [mark_deleted, mark_active]
    list_display = [
        "name",
        "barcode",
        "item_number",
        "subcategory",
        "list_price",
        "is_hot_product",
        "is_new_arrival",
    ]
    list_filter = [
        "subcategory",
        "is_hot_product",
        "is_new_arrival",
        "is_deleted",
    ]
    search_fields = ["name", "barcode", "item_number"]
    autocomplete_fields = ["creator", "subcategory", "available_regions"]
    something = [ "subcategory_name", "available_regions_list"]


@admin.register(ProductWishList)
class ProductWishListAdmin(ImportExportActionModelAdmin):
    actions = [mark_deleted, mark_active]
    list_display = ["product", "user"]
    search_fields = ["product"]
    autocomplete_fields = ["user"]
