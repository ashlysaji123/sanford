from django import forms
from django.forms.widgets import (
    DateInput,
    FileInput,
    NumberInput,
    Select,
    Textarea,
    TextInput,
    EmailInput
)

from accounts.models import User

from .models import (
    GlobalManager,
    GlobalManagerTarget,
    GlobalManagerTask,
)


class GlobalManagerForm(forms.ModelForm):
    class Meta:
        model = GlobalManager
        exclude = ("user", "is_deleted", "creator")
        widgets = {
            "name": TextInput(
                attrs={"class": "required form-control", "placeholder": "Name"}
            ),
            "employe_id": TextInput(
                attrs={"class": "required form-control", "placeholder": "Employe ID"}
            ),
            "phone": TextInput(
                attrs={"class": "required form-control", "placeholder": "Phone"}
            ),
            "city": TextInput(attrs={"class": " form-control", "placeholder": "City"}),
            "address": Textarea(
                attrs={"class": " form-control", "placeholder": "Address"}
            ),
            "dob": DateInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Date of Birth",
                    "id": "Date",
                    "name": "date",
                    "type": "date",
                }
            ),
            "photo": FileInput(attrs={"class": "form-control"}),
            "location": TextInput(
                attrs={"class": "form-control", "placeholder": "Location"}
            ),
            "visa_number": TextInput(
                attrs={"class": "form-control", "placeholder": "Visa number"}
            ),
            "visa_expiry": DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Visa expiry",
                    "id": "Date",
                    "name": "date",
                    "type": "date",
                }
            ),
            "passport_number": TextInput(
                attrs={"class": " form-control", "placeholder": "Passport number"}
            ),
            "passport_expiry": DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Passport expiry",
                    "id": "Date",
                    "name": "date",
                    "type": "date",
                }
            ),
            "region": Select(attrs={"class": "required form-control tt-select2"}),

            "staff_type": Select(attrs={"class": "required form-control tt-select2"}),
            "department": Select(attrs={"class": "required form-control tt-select2"}),
            "designation": Select(attrs={"class": "required form-control tt-select2"}),
            "email": EmailInput(
                attrs={"class": "required form-control", "placeholder": "E-mail"}
            ),
            "salary": TextInput(
                attrs={"class": "required form-control", "placeholder": "Salary amount"}
            ),
        }


class GlobalManagerTargetForm(forms.ModelForm):
    class Meta:
        model = GlobalManagerTarget
        fields = ("year", "month", "target_amount", "target_type", "user")
        widgets = {
            "user": Select(attrs={"class": "required form-control tt-select2"}),
            "year": Select(attrs={"class": "required form-control tt-select2"}),
            "month": Select(attrs={"class": "required form-control tt-select2"}),
            "target_amount": NumberInput(
                attrs={"class": "required form-control", "placeholder": "Target amount"}
            ),
            "target_type": Select(attrs={"class": "required form-control tt-select2"}),
        }


class GlobalManagerTaskForm(forms.ModelForm):
    class Meta:
        model = GlobalManagerTask
        fields = ("task", "user")
        widgets = {
            "task": TextInput(
                attrs={"class": "required form-control", "placeholder": "Task"}
            ),
            "user": Select(attrs={"class": "required form-control tt-select2"}),
        }

