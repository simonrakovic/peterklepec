# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import EmailValidator


class QuestionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'invalid': 'Nepravilen e-poštni nsalov.','required': 'Prosim vnesite svoj e-poštni naslov.' })
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), error_messages={'required': 'Prosim, vnesite vprašanje.' })