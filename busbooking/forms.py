from dataclasses import fields
from email.mime import image
from django import forms
from django.forms import ModelForm
from . models import donate

class donateform(ModelForm):
    Name = forms.TextInput()
    City = forms.TextInput()
    Type = forms.TextInput()
    Area = forms.TextInput()
    Mobile = forms.NumberInput()
    class Meta:
        model =donate
        fields=['Name','Type','Area','Mobile','City']