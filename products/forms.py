from django import forms
from django.forms.widgets import CheckboxInput, FileInput, Select, Textarea, TextInput
from tinymce.widgets import TinyMCE

from .models import Category, Product, ProductGroup, SubCategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name", "code", "icon", "image")
        widgets = {
            "name": TextInput(
                attrs={"class": "required form-control", "placeholder": "Category Name"}
            ),
            "icon": FileInput(attrs={"class": "required form-control"}),
            "image": FileInput(attrs={"class": "required form-control"}),
            "code": TextInput(
                attrs={"class": "required form-control", "placeholder": "Category Code"}
            ),
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ("category", "name", "code")
        widgets = {
            "category": Select(attrs={"class": "required form-control tt-select2"}),
            "name": TextInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Sub Category Name",
                }
            ),
            "code": TextInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "ub Category Code",
                }
            ),
        }


class ProductGroupForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        fields = ("name", "code", "icon")
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Sub Category Name",
                }
            ),
            "code": TextInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "ub Category Code",
                }
            ),
            "icon": FileInput(attrs={"class": "required form-control"}),
        }


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}))

    class Meta:
        model = Product
        exclude = ("user", "is_deleted", "creator")
        widgets = {
            "name": TextInput(
                attrs={"class": "required form-control", "placeholder": "Product name"}
            ),
            "barcode": TextInput(
                attrs={"class": "required form-control", "placeholder": "Barcode"}
            ),
            "item_number": TextInput(
                attrs={"class": "required form-control", "placeholder": "Item number"}
            ),
            "summary": Textarea(
                attrs={"class": " form-control", "placeholder": "Summary"}
            ),
            "group": Select(attrs={"class": "required form-control tt-select2"}),
            "subcategory": Select(attrs={"class": "required form-control tt-select2"}),
            "list_price": TextInput(
                attrs={"class": "required form-control", "placeholder": "List price"}
            ),
            "primary_image": FileInput(attrs={"class": "required form-control"}),
            "feature_graphic": FileInput(attrs={"class": "required form-control"}),
            "product_pdf": FileInput(attrs={"class": "form-control"}),
            "is_hot_product": CheckboxInput(attrs={"class": ""}),
            "is_new_arrival": CheckboxInput(attrs={"class": ""}),
            "is_out_of_stock": CheckboxInput(attrs={"class": ""}),
            "available_regions": forms.CheckboxSelectMultiple(attrs={"class": ""}),
        }
