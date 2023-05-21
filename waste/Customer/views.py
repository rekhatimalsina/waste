from django.http import JsonResponse
from django.shortcuts import redirect,render,HttpResponse
from django.views.generic import  CreateView,TemplateView,FormView,View
import requests
from .forms import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from . import service
from .models import AddBins
from Driver.models import Driver
import geocoder
from haversine import haversine, Unit
from django.shortcuts import render, get_object_or_404
from .models import AddBins, Order
from django.core.paginator import Paginator



class CustomerRegistration(CreateView):
    template_name = "registration.html"
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy("Customer:customer-login")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
        

def listDriver(request):
    driver=Driver.objects.all()
    data={
        'driver':driver
    }
    return render(request,'driver.html',data)


def binList(request):
    user = request.user
    bin = AddBins.objects.filter(user=user).all()
    paginator = Paginator(bin, 8)
    data = {
        'bin':bin,
    }
    return render(request,'binlist.html',data)


def bin_create(request):
    data = {
        'title' : 'bin',
        'driver':Driver.objects.all(),   
    }
    return render(request,'addbin.html', data)

def order_create(request):
    data = {
        'title' : 'bin',
         
    }
    return render(request,'orderadd.html', data)


def bin_store(request):
    service.Addbin(request)
    return redirect("Customer:bin.list")



def getDriverGroupList():
    return Driver.objects.all()


def bin_edit(request, id):  
    bin = service.getBinId(id)
    print(bin)
    data = {
        'title' : 'Item',
        'driver':Driver.objects.all(),
        
        'bin' : bin
    }
    return render(request,'addbin.html',data)


def bin_update(request, id):  
    service.updateBin(request,id)
    return redirect('bin.list')


def bin_delete(request, id):  
    service.deleteBin(request,id)
    return redirect('bin.list')


class CustomerLoginView(FormView):
    template_name = "CustomerLogin.html"
    form_class = CustomerLoginForm
    success_url = reverse_lazy("Customer:bin.create")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Customer.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
        
class CustomerProfileView(TemplateView):
    template_name = "Customerprofile.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        context['customer'] = customer
        return context
    

class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("Customer:customer-login")
    
def order_view(request,id):
    bin = get_object_or_404(AddBins, pk=id)
    g = geocoder.ip('me')
    if(bin.status =="Accept"):
        if request.method == 'POST':
            point1 = (g.lat, g.lng) 
            print(point1) 
            point2 = (27.67276991918297, 85.31843887356557) 
            distance = haversine(point1, point2, unit=Unit.KILOMETERS)
            print(distance)
            total = 20 * distance
            payment_method=request.POST['payment_method']
            order = Order(user=request.user, bin=bin, total=total,payment_method=payment_method)
            print(order)
            order.save()
            return redirect('Customer:order.payment',id)
            #return render(request, 'orderList.html', {'order': order}) 
    else:
        return HttpResponse("invalide request")   
    return render(request, 'order_form.html', {'bin': bin})


def orderList(request):
    user = request.user
    print(user)
    order = Order.objects.filter(user=user).all()
    data={
        'order':order 
    }
    return render(request,'orderList.html',data)


def get_lat_long(request):
    lat_long_data = {
        "latitude": 37.7749,
        "longitude": -122.4194
    }
    return JsonResponse(lat_long_data)

def payment(request,id): 
    order = service.getOrderId(id)
    print(order)
    data = {
        'title' : 'Item', 
        'order' : order
    }
    return render(request,'payment.html',data)
