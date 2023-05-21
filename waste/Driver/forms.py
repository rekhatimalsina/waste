from django import forms
from Customer.models import AddBins
from .models import  Driver,Appointment
from django.contrib.auth.models import User

class DriverRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    
    class Meta:
        model = Driver
        fields = ["driver_full_name","username","address","email", "password","license_no", "image","license_photo",]

class DriverLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'patient_name', 'description']


class AddBin1s(forms.ModelForm):
    class Meta:
        model = AddBins
        fields=['status']