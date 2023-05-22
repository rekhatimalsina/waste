from django.contrib.auth.models import User
from Driver.models import Driver
from .models import AddBins, Order
from .models import Customer

import geocoder
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def AddOrder(self,request):
    order=Order(
    customer = self.request.user.customer,
    )

def Addbin(request):
    user=request.user
    print(user)
    g = geocoder.ip('me')
    bin=AddBins(
        user=request.user,
        driver             =Driver.objects.get(pk=request.POST['driver']),
        grabage_type        =request.POST.get('grabage_type',False),
        address              =request.POST.get('address',False),
        latitude           = g.lat,
        longitude           = g.lng,
        created_at              =request.POST.get('created_at',False),
        updated_at              =request.POST.get('updated_at',False), 
    )
    bin.save()
    return "sucess"



def AddOrder(request):
    bin=AddBins(
        customer                = Customer.objects.customer_id,
        bin                     =AddBins.objects.bin_id,
        total        =request.POST.get('total',False),
        address              =request.POST.get('address',False),
        payment_method             =request.POST.get('payment_method',False),
        payment_completed          =request.POST.get('payment_completed',False),
        created_at              =request.POST.get('created_at',False),
        updated_at              =request.POST.get('updated_at',False),       
        
    )
    print(bin)
    bin.save()
    return "sucess"

def updateBin(request,id):

    bin =AddBins.objects.get(id =id)
    bin.grabage_type                   =request.POST.get('grabage_type',False)
    bin.address                  =request.POST.get('address',False)
    bin.latitude               =request.POST.get('latitude',False)
    bin.longitude          =request.POST.get('longitude',False)    
    bin.driver =   Driver.objects.get(pk=request.POST['driver'])
    bin.save()
    return "Sucess"

def deleteBin(request,id):
    bin = AddBins.objects.get(id = id)
    bin.delete()
    return "success"


def listBin(request):
     return AddBins.objects.all()


def listDriver(request):
    return Driver.objects.all()

def getBinId(id):
    bin = AddBins.objects.get(id= id)
    return bin

def AddOrder(request):
    order=Order(
        customer=request.user,
        total        =request.POST.get('total',False),
        payment_method              =request.POST.get('payment_method',False),
        payment_completed             =request.POST.get('payment_completed',False),   
    )
    order.save()
    return order

def getOrderId(id):
    bin = Order.objects.get(id= id)
    return bin