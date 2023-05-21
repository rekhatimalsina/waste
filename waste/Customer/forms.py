from django import forms
from .models import  Customer ,AddBins
from django.contrib.auth.models import User
from .models import Order

class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    
    class Meta:
        model = Customer
        fields = ["customer_full_name","username", "password", "email","image","address"]


class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class addBin(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = AddBins
        fields = "__all__"
