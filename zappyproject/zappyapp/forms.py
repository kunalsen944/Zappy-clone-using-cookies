from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer,Order


class CustomerUpdate(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['images','cust_address','mobile',]


class Checkout(forms.ModelForm):
    delievery_address=forms.CharField(required=False)
    class Meta:
        model=Order
        widgets = {'delievery_address': forms.TextInput(attrs={'placeholder': 'Same as Billing Address'})}
        fields=['delievery_address']
