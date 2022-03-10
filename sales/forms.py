from django import forms
from django.forms.widgets import Select, TextInput

from merchandiser.models import Merchandiser

from .models import OpeningStock


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
        if not user.is_superuser:
            self.fields["merchandiser"].queryset = Merchandiser.objects.filter(
                user__region=user.region
            )
