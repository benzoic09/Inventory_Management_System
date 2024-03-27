from django.contrib import admin
from .models import devicetype, Devices, employees

# Register your models here.
admin.site.register(devicetype)
admin.site.register(Devices)
admin.site.register(employees)