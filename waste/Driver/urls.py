from django.urls import path
from .views import *
from . import views


app_name = "Driver"
urlpatterns = [
    path("register/",DriverRegistration.as_view(), name="driver-registration"),
    
    path("login/",DriverLoginView.as_view(), name="driver-login"),
    path("profile/",DriverProfileView.as_view(), name="driver-profile"),
    path("logout/",DriverLogoutView.as_view(), name="driver-logout"),
    path('',views.front,name="front"),
    path('driverbin/',views.listBins,name="driver-binlist"),
    path('editDriverBins/<int:id>',views.editbins,name="driver-editBins"),
    path('updatebinsdriver/<int:id>',views.DriverUpdatebins,name="driver-binupdate"),
    path('driveracceptbin/',views.listBins,name="driver-acceptbinlist"),
    # path('map/', views.googlemap, name='map'),


]