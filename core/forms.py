from django import forms
from django.forms.widgets import Select, TextInput

from core.models import Country, Language, Region, Shop, State


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ("name",)


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ("family", "name", "native_name", "lang_code")


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = (
            "name",
            "country_code",
            "region",
        )


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ("name", "type", "country", "state_code", "tin_number")


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = (
            "name",
            "location",
            "contact_number",
            "contact_number2",
            "country",
            "state",
        )
