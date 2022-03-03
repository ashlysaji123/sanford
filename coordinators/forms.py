from django import forms
from django.forms.widgets import (DateInput, EmailInput, FileInput, Select,
                                  Textarea, TextInput,NumberInput)

from .models import *



class SalesManagerForm(forms.ModelForm):
	class Meta:
		model = SalesManager
		exclude = ('user','is_deleted','creator')
		widgets = {
			'name' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
			'employe_id' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Employe ID'}),
			'phone' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone'}),
			'city' :TextInput(attrs={'class': ' form-control', 'placeholder': 'City'}),
			'address' :Textarea(attrs={'class': ' form-control', 'placeholder': 'Address'}),
            'dob': DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'id': 'Date', 'name': 'date', 'type': 'date'}),
            'photo': FileInput(attrs={'class': 'form-control'}),
			'location' :TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
			'visa_number' :TextInput(attrs={'class': 'form-control', 'placeholder': 'Visa number'}),
            'visa_expiry': DateInput(attrs={'class': 'form-control', 'placeholder': 'Visa expiry', 'id': 'Date', 'name': 'date', 'type': 'date'}),
			'passport_number' :TextInput(attrs={'class': ' form-control', 'placeholder': 'Passport number'}),
            'passport_expiry': DateInput(attrs={'class': 'form-control', 'placeholder': 'Passport expiry', 'id': 'Date', 'name': 'date', 'type': 'date'}),
            'region': Select(attrs={'class': 'required form-control tt-select2'}),
        }

class SalesManagerTargetForm(forms.ModelForm):
	class Meta:
		model = SalesManagerTarget
		fields = ('year','month','target_amount','target_type','user')
		widgets = {
            'user' :Select(attrs={'class': 'required form-control tt-select2'}),
            'year': Select(attrs={'class': 'required form-control tt-select2'}),
            'month': Select(attrs={'class': 'required form-control tt-select2'}),
			'target_amount' :NumberInput(attrs={'class': 'required form-control', 'placeholder': 'Target amount'}),
			'target_type' :Select(attrs={'class': 'required form-control tt-select2'}),
		}

class SalesManagerTaskForm(forms.ModelForm):
	class Meta:
		model = SalesManagerTask
		fields = ('task','user')
		widgets = {
			'task' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Task'}),
            'user' :Select(attrs={'class': 'required form-control tt-select2'}),
		}


class SalesCoordinatorForm(forms.ModelForm):
	class Meta:
		model = SalesCoordinator
		exclude = ('user','is_deleted','creator')
		widgets = {
			'name' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
			'employe_id' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Employe ID'}),
			'phone' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone'}),
			'city' :TextInput(attrs={'class': ' form-control', 'placeholder': 'City'}),
			'address' :Textarea(attrs={'class': ' form-control', 'placeholder': 'Address'}),
            'dob': DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'id': 'Date', 'name': 'date', 'type': 'date'}),
            'photo': FileInput(attrs={'class': 'form-control'}),
			'visa_number' :TextInput(attrs={'class': 'form-control', 'placeholder': 'Visa number'}),
            'visa_expiry': DateInput(attrs={'class': 'form-control', 'placeholder': 'Visa expiry', 'id': 'Date', 'name': 'date', 'type': 'date'}),
			'passport_number' :TextInput(attrs={'class': ' form-control', 'placeholder': 'Passport number'}),
            'passport_expiry': DateInput(attrs={'class': 'form-control', 'placeholder': 'Passport expiry', 'id': 'Date', 'name': 'date', 'type': 'date'}),
            'region': Select(attrs={'class': 'required form-control tt-select2'}),
        }

class SalesCoordinatorTargetForm(forms.ModelForm):
	class Meta:
		model = SalesCoordinatorTarget
		fields = ('year','month','target_amount','target_type','user')
		widgets = {
            'user' :Select(attrs={'class': 'required form-control tt-select2'}),
            'year': Select(attrs={'class': 'required form-control tt-select2'}),
            'month': Select(attrs={'class': 'required form-control tt-select2'}),
			'target_amount' :NumberInput(attrs={'class': 'required form-control', 'placeholder': 'Target amount'}),
			'target_type' :Select(attrs={'class': 'required form-control tt-select2'}),
		}

class SalesCoordinatorTaskForm(forms.ModelForm):
	class Meta:
		model = SalesCoordinatorTask
		fields = ('task','user')
		widgets = {
			'task' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Task'}),
            'user' :Select(attrs={'class': 'required form-control tt-select2'}),
		}
