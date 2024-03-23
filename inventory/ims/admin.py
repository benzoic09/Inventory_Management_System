from django.contrib import admin
from .models import devicetype, devices, employees, branch

# Register your models here.
admin.site.register(devicetype)
admin.site.register(devices)
admin.site.register(employees)
admin.site.register(branch)