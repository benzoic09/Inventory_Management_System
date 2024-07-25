from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('devtype/', views.devicetype_list, name='device_type'),
    path('adddevice/', views.add_device, name='add_device'),
    path('employees/', views.employee_list, name='employee_list'),
    path('addemployee/', views.add_employee, name='add_employee'),
    path('add_assignment/',views.add_assignment, name='add_asssignment'),

    # add/edit/delete devices 
    path('devices/',views.device_list, name='device_list'),
    path('add_device_type/', views.add_device_type, name='add_device_type'),
    path('devices/edit/<int:id>', views.edit_device, name='edit_device'),
    path('devices/delete/<int:id>', views.delete_device, name='delete_device'),

]