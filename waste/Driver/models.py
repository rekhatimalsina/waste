from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    driver_full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="driver/images/")
    joined_on = models.DateTimeField(auto_now_add=True)
    license_no=models.CharField(max_length=200, null=True, blank=True)
    license_photo = models.ImageField(upload_to="driver/images/")
    latitude1 = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude1 = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def str(self):
        return self.full_name
    
class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    patient_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)