from django.db import models
from django.contrib.auth.models import User
# from Driver.models import Driver

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="customer/images/")
    joined_on = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.full_name
    


class AddBins(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grabage_type=models.CharField(max_length=200,default=0)
    address=models.CharField(max_length=200,default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    driver=models.ForeignKey('Driver.Driver',on_delete=models.CASCADE)
    status = models.CharField(max_length=30,default="pending")
    created_at                 = models.DateTimeField(auto_now_add=True)
    updated_at                 = models.DateTimeField(auto_now=True)
METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Khalti", "Khalti"),
   
)

class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   bin= models.ForeignKey(AddBins,on_delete=models.CASCADE)
   total=models.PositiveIntegerField()
   payment_method = models.CharField(max_length=20, choices=METHOD, default="Cash On Delivery")
   payment_completed = models.BooleanField(default=False, null=True, blank=True)
   def str(self):
        return f"{self.user.username} - {self.bin.address}"