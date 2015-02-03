from django import forms
from .models import doyouknow
from django.forms import ModelForm

class doyouknowForm(forms.ModelForm):
    class Meta:
        model=doyouknow
        fields = ['picture']