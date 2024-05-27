from django import forms
from indian_states.models import State

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name', 'population', 'language', 'capital']
