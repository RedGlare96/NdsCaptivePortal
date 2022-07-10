from django import forms
from django.forms import ModelForm
from .models import Client


class reg_form(ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'plan']