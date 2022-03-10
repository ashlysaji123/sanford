from django import forms
from django.forms.widgets import Select, Textarea, TextInput

from .models import Notification


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ("title", "type", "description")
        widgets = {
            "title": TextInput(
                attrs={"class": "required form-control", "placeholder": "Title"}
            ),
            "type": Select(attrs={"class": "required form-control tt-select2"}),
            "description": Textarea(
                attrs={"class": "required form-control", "placeholder": "Message"}
            ),
        }
