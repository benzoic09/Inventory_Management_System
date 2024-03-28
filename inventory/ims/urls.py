from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('devtype/', views.devicetype_list, name='device_type'),
    path('add_device_type/', views.add_device_type, name='add_device_type'),
    path('devices/',views.device_list, name='device_list'),
    path('adddevice/', views.add_device, name='add_device'),
    path('employees/', views.employee_list, name='employee_list'),
    path('addemployee/', views.add_employee, name='add_employee'),

]