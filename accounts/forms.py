from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

# Example OrderForm


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','status']


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']