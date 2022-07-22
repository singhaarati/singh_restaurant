from dataclasses import field
from django import forms
from owner.models import Owner
class OwnerForms(forms.ModelForm):
    class Meta:
        model=Owner
        fields="__all__"