#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from appproyecto.models import usuario

class registroForm(ModelForm):
    class Meta:
        model = usuario