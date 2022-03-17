from django import forms
from django.forms.widgets import Select, DateInput

from votings.models import Voting,VotingItem

class VotingItemForm(forms.ModelForm):

    class Meta:
        model = VotingItem
        fields = ('product', 'voting_startdate', 'voting_enddate')
        widgets = {
            "product": Select(
                attrs={"class": "required form-control tt-select2"}
            ),
            "voting_startdate": DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "voting_startdate",
                    "id": "Date",
                    "name": "date",
                    "type": "date",
                }
            ),
            "voting_enddate": DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "voting_enddate",
                    "id": "Date",
                    "name": "date",
                    "type": "date",
                }
            ),
        }
