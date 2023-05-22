from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from django.views.generic import  CreateView,FormView,TemplateView,View
from django.contrib import messages
from Customer.models import AddBins
from .forms import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
import geocoder
from django.http import HttpResponse
import csv
from . import service
# Create your views here.
class DriverRegistration(CreateView):
    template_name = "registration1.html"
    form_class = DriverRegistrationForm
    success_url = reverse_lazy("Driver:driver-profile")
    
    def form_valid(self, form): 
        g = geocoder.ip('me')
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        form.instance.latitude1 =g.lat
        form.instance.longitude1 = g.lng
        driver=form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
    

def front(request):
    return render(request,'Front.html')


class DriverLoginView(FormView):
    template_name = "DriverLogin.html"
    form_class = DriverLoginForm
    success_url = reverse_lazy("Driver:driver-binlist")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Driver.objects.filter(user=usr).exists():
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
        

class DriverProfileView(TemplateView):
    template_name = "Driverprofile.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Driver.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        driver = self.request.user.driver
        context['driver'] = driver
        #orders = Order.objects.filter(cart__customer=customer).order_by("-id")
        #context["orders"] = orders
        return context
    
class DriverLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("Driver:driver-login")

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Driver:appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

def listBins(request):
    user = request.user
    print(user)
    driver = Driver.objects.get(user=user)
    bin = AddBins.objects.filter(driver=driver).select_related('driver') 
    data={
        'bin':bin 
    }
    return render(request,'Binlist1.html',data)

def listBins1(request):
    user = request.user
    print(user)
    driver = Driver.objects.get(user=user)
    bin = AddBins.objects.filter(driver=driver).select_related('driver') 
    data={
        'bin':bin 
    }
    return render(request,'locationTrap.html',data)

def editbins(request, id):
    bins = AddBins.objects.get(id=id)
    if(bins.status != "Accept" and bins.status != "Decline" ):
        form = AddBin1s(request.POST or None, request.FILES or None, instance=bins)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('name')} has been added")
            return redirect('Driver:driver-binlist')
        context = {
            'form': form,
        }
        print(context)
        return render(request, 'updatebin.html', context)
    else:
        form = AddBin1s(request.POST or None, request.FILES or None, instance=bins)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('name')} has been added")
            return redirect('Driver:driver-binlist')
        context = {
            'form': form,
        }
        print(context)
        return render(request, 'updatebin1.html', context)



def DriverUpdatebins(request):
    update=service.updateBins(request,id)
    print(update)
    return redirect('Driver:driver-binlist')


def acceptList(request):
    user = request.user
    print(user)
    driver = Driver.objects.get(user=user)
    bin = AddBins.objects.filter(status="ACCEPT").all()
    data={
        'bin':bin 
    }
    return render(request,'acceptBin.html',data)


def map_view(request,id):
    addbin=AddBins.objects.get(id=id) 
    # Retrieve latitude and longitude data for two different places from your backend source
    g = geocoder.ip('me')
    place1_latitude=g.lat
    place1_longitude = g.lng
    place2_latitude =addbin.latitude
    place2_longitude = addbin.longitude
 # Pass the location data to the template
    context = {
        'place1_latitude': place1_latitude,
        'place1_longitude': place1_longitude,
        'place2_latitude': place2_latitude,
        'place2_longitude': place2_longitude,
    }
    print(context)

    return render(request, 'map1.html', context)

def customerlist(request):
    user = request.user
    print(user)
    driver = Driver.objects.get(user=user)
    bin = AddBins.objects.filter(driver=driver).select_related('driver') 
    data={
        'bin':bin 
    }
    return render(request,'customerlist.html',data)