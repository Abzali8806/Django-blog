from dataclasses import fields
from django import forms

from .models import Space

class CreateSpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = [
            'title',
            'rules',
            'intro'
        ]