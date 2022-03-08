from django import forms
from django.forms.widgets import (DateInput, EmailInput, FileInput, Select,
                                  Textarea, TextInput,NumberInput)
from location_field.forms.plain import PlainLocationField

from core.models import Language,Region,Country,State,Shop



class RegionForm(forms.ModelForm):
	class Meta:
		model = Region
		fields = ('name',)
		widgets = {
			'name' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Region Name'}),
		}

class LanguageForm(forms.ModelForm):
	class Meta:
		model = Language
		fields = ('family','name','native_name','lang_code')
		widgets = {
			'family' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Family'}),
			'name' :TextInput(attrs={'class': 'required form-control', 'placeholder': ' Name'}),
			'native_name' :TextInput(attrs={'class': ' form-control', 'placeholder': 'Native Name'}),
			'lang_code' :TextInput(attrs={'class': ' form-control', 'placeholder': 'Language code'}),
		}

class CountryForm(forms.ModelForm):
	class Meta:
		model = Country
		fields = ('name','country_code','region',)
		widgets = {
			'name' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
			'country_code' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Country code'}),
			'region' :Select(attrs={'class': 'required form-control tt_select2'}),
		}

class StateForm(forms.ModelForm):
	class Meta:
		model = State
		fields = ('name','type','country','state_code','tin_number')
		widgets = {
			'name' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
			'type' :Select(attrs={'class': 'required form-control tt_select2'}),
			'country' :Select(attrs={'class': 'required form-control tt_select2'}),
			'state_code' :TextInput(attrs={'class': 'form-control', 'placeholder': 'State code'}),
			'tin_number' :TextInput(attrs={'class': 'form-control', 'placeholder': 'Tin number'}),
		}

class ShopForm(forms.ModelForm):
	class Meta:
		model = Shop
		fields = ('name','location','contact_number','contact_number2','country','state')
		widgets = {
			'name' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
			# 'location' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Location'}),
			'contact_number' :TextInput(attrs={'class': 'required form-control', 'placeholder': 'Contact number'}),
			'contact_number2' :TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact number'}),
			'country' :Select(attrs={'class': 'required form-control tt_select2'}),
			'state' :Select(attrs={'class': 'required form-control tt_select2'}),
		}
