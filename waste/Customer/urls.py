from django.urls import path
from .views import *
from . import views


app_name = "Customer"
urlpatterns = [
    path("customerRegister/",
         CustomerRegistration.as_view(), name="customer-registration"),
    path("login/",CustomerLoginView.as_view(), name="customer-login"),
    path("profile/",CustomerProfileView.as_view(), name="customer-profile"),
    path('driverlist/',views.listDriver,name="customer-driverlist"),
    path("logout/",CustomerLogoutView.as_view(), name="customer-logout"),


    path('binList/', views.binList, name='bin.list'),
    path('addBin/', views.bin_create, name='bin.create'),
    path('binstore/', views.bin_store, name='bin.store'),
    path('edit/<int:id>', views.bin_edit, name='bin.edit'),
    path('update/<int:id>', views.bin_update, name='bin.update'),
    path('delete/<int:id>', views.bin_delete, name='bin.delete'),

    path('orderList/', views.orderList, name='order.list'),
    path('addorder/<int:id>', views.order_view, name='order.create'),
    path('payment/<int:id>',views.payment,name="order.payment"),
    path('lati',views.get_lat_long,name='lat'),
    path('driverlocation/<int:id>', views.customerMap, name='drivermap'),
]