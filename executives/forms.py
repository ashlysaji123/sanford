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
    SalesExecutive, 
    SalesExecutiveTarget, 
    SalesExecutiveTask,
    SalesSupervisor,
    SalesSupervisorTarget,
    SalesSupervisorTask
)


class SalesSupervisorForm(forms.ModelForm):
    class Meta:
        model = SalesSupervisor
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
            "sub_region": Select(attrs={"class": "required form-control tt-select2"}),

            "company": Select(attrs={"class": "required form-control tt-select2"}),
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


class SalesSupervisorUpdateForm(forms.ModelForm):
    class Meta:
        model = SalesSupervisor
        exclude = ("user", "is_deleted", "creator","phone")
        widgets = {
            "name": TextInput(
                attrs={"class": "required form-control", "placeholder": "Name"}
            ),
            "employe_id": TextInput(
                attrs={"class": "required form-control", "placeholder": "Employe ID"}
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
            "sub_region": Select(attrs={"class": "required form-control tt-select2"}),

            "company": Select(attrs={"class": "required form-control tt-select2"}),
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


class SalesSupervisorTargetForm(forms.ModelForm):
    class Meta:
        model = SalesSupervisorTarget
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

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (user.is_superuser or user.is_global_manager):
            self.fields["user"].queryset = SalesSupervisor.objects.filter(
                region=user.region)


class SalesSupervisorTaskForm(forms.ModelForm):
    class Meta:
        model = SalesSupervisorTask
        fields = ("task", "user")
        widgets = {
            "task": TextInput(
                attrs={"class": "required form-control", "placeholder": "Task"}
            ),
            "user": Select(attrs={"class": "required form-control tt-select2"}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (user.is_superuser or user.is_global_manager):
            self.fields["user"].queryset = SalesSupervisor.objects.filter(
                region=user.region)



class SalesExecutiveForm(forms.ModelForm):
    class Meta:
        model = SalesExecutive
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
            "supervisor": Select(attrs={"class": "required form-control tt-select2"}),
            "region": Select(attrs={"class": "required form-control tt-select2"}),
            "sub_region": Select(attrs={"class": "required form-control tt-select2"}),

            "company": Select(attrs={"class": "required form-control tt-select2"}),
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

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (user.is_superuser or user.is_global_manager):
            self.fields["supervisor"].queryset = SalesSupervisor.objects.filter(
                region=user.region)


class SalesExecutiveUpdateForm(forms.ModelForm):
    class Meta:
        model = SalesExecutive
        exclude = ("user", "is_deleted", "creator","phone")
        widgets = {
            "name": TextInput(
                attrs={"class": "required form-control", "placeholder": "Name"}
            ),
            "employe_id": TextInput(
                attrs={"class": "required form-control", "placeholder": "Employe ID"}
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
            "supervisor": Select(attrs={"class": "required form-control tt-select2"}),
            "region": Select(attrs={"class": "required form-control tt-select2"}),
            "sub_region": Select(attrs={"class": "required form-control tt-select2"}),

            "company": Select(attrs={"class": "required form-control tt-select2"}),
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

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (user.is_superuser or user.is_global_manager):
            self.fields["supervisor"].queryset = SalesSupervisor.objects.filter(
                region=user.region)




class SalesExecutiveTargetForm(forms.ModelForm):
    class Meta:
        model = SalesExecutiveTarget
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

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (user.is_superuser or user.is_global_manager):
            self.fields["user"].queryset = SalesExecutive.objects.filter(
                region=user.region)


class SalesExecutiveTaskForm(forms.ModelForm):
    class Meta:
        model = SalesExecutiveTask
        fields = ("task", "user")
        widgets = {
            "task": TextInput(
                attrs={"class": "required form-control", "placeholder": "Task"}
            ),
            "user": Select(attrs={"class": "required form-control tt-select2"}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (user.is_superuser or user.is_global_manager):
            self.fields["user"].queryset = SalesExecutive.objects.filter(
                region=user.region)
