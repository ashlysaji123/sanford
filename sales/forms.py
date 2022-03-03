from django import forms
from django.forms.widgets import (DateInput, EmailInput, FileInput, Select,
                                  Textarea, TextInput,NumberInput,CheckboxInput)

from .models import *



class OpeningStockForm(forms.ModelForm):
    class Meta:
        model = OpeningStock
        fields = ('merchandiser','product','count')
        widgets = {
            'merchandiser': Select(attrs={'class': 'required form-control tt-select2'}),
            'product': Select(attrs={'class': 'required form-control tt-select2'}),
            'count' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'OpeningStock Count'}),
        }
