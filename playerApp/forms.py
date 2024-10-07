from django import forms
from .models import Default

class DefaultForm(forms.ModelForm):
    class Meta:
        model = Default
        fields = ['name', 'fire', 'water', 'ground', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 300px;'}),
            'fire': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 4, 'style': 'width: 300px;'}),
            'water': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 4, 'style': 'width: 300px;'}),
            'ground': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 4, 'style': 'width: 300px;'}),
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 40}), 
        }
