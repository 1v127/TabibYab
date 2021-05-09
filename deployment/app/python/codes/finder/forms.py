from django import forms
from . import models


attr = {'class': 'form-control'}


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name', 'family', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs=attr),
            'family': forms.TextInput(attrs=attr),
            'email': forms.EmailInput(attrs=attr),
            'message': forms.Textarea(attrs=attr)
        }
