from django import forms
from . import models


class ModelForm(forms.ModelForm):

    class Meta:
        model = models.Model
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':3})
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }