from django import forms
from django.forms.widgets import Select, TextInput
from django.db.models import Q

from merchandiser.models import Merchandiser

from .models import OpeningStock,Sales
from accounts.models import User

class SelectStaffForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ("user",)
        widgets = {
            "user": Select(attrs={"class": "required form-control tt-select2"}),
        }
        labels = {
            'user': "Staff"
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (user.is_superuser or user.is_global_manager):
            queryset = User.objects.filter(Q(is_sales_executive=True) | Q(is_merchandiser=True))
            self.fields["user"].queryset = queryset.filter(
                region=user.region
            )

class OpeningStockForm(forms.ModelForm):
    class Meta:
        model = OpeningStock
        fields = ("merchandiser", "product", "count")
        widgets = {
            "merchandiser": Select(attrs={"class": "required form-control tt-select2"}),
            "product": Select(attrs={"class": "required form-control tt-select2"}),
            "count": TextInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "OpeningStock Count",
                }
            ),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (user.is_superuser or user.is_global_manager):
            self.fields["merchandiser"].queryset = Merchandiser.objects.filter(
                user__region=user.region
            )
