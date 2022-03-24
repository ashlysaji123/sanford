from django import forms
from django.forms.widgets import DateInput, NumberInput, Select, TextInput

from core.models import Shop
from executives.models import SalesExecutive

from .models import DARNotes, DARTask


class DARTaskForm(forms.ModelForm):
    class Meta:
        model = DARTask
        fields = ("executive", "shop", "visit_date", "available_time")
        widgets = {
            "executive": Select(attrs={"class": "required form-control tt-select2"}),
            "shop": Select(attrs={"class": "required form-control tt-select2"}),
            "visit_date": DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Date",
                    "id": "Date",
                    "name": "date",
                    "type": "date",
                }
            ),
            "available_time": NumberInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Available time",
                }
            ),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (user.is_superuser or user.is_global_manager):
            self.fields["executive"].queryset = SalesExecutive.objects.filter(
                region=user.region, is_deleted=False
            )
            self.fields["shop"].queryset = Shop.objects.filter(
                country__region=user.region, is_deleted=False
            )


class DARNotesForm(forms.ModelForm):
    class Meta:
        model = DARNotes
        fields = ("title", "note")
        widgets = {
            "title": TextInput(
                attrs={"class": "required form-control", "placeholder": "Title"}
            ),
            "note": TextInput(attrs={"class": "form-control", "placeholder": "Note"}),
        }
