from .models import Station, StationTag
from django import forms
from django.forms import formset_factory, inlineformset_factory


class StationRainModelForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ["title", "city", "recent_rainfall"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'recent_rainfall': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
        }