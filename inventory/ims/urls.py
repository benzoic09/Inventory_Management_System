from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('devtype/', views.devicetype_list, name='devicetype'),
#     path('devices/', views.devices_list, name='devices_list'),
#     path('employees/', views.employees_list, name='employees_list'),
]