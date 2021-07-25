from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import forms
from application import models

class apply(forms.ModelForm):
      class Meta:
         model = models.Application
         fields = '__all__'