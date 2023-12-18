from .models import *
from django import forms

# Example OrderForm


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','status']
