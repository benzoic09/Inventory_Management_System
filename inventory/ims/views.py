from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import devicetype, Devices, employees
from .forms import DeviceTypeForm, DeviceForm, EmployeeForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to index page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'login_form': form})


def home(request):
    return render(request, 'home.html')

def devicetype_list(request):
    devicetypes = devicetype.objects.all()
    return render(request, 'devicetype_list.html', {'devicetypes': devicetypes})

# Devices  
def add_device_type(request):
    if request.method == 'POST':
        form = DeviceTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_type')
    else:
        form = DeviceTypeForm()
        return render(request, 'add_device_type.html', {'form': form})

def device_list(request):
    device_list = Devices.objects.all()
    return render(request, 'devices.html', {'devices': device_list})


def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
        return render(request, 'add_device.html', {'form': form})
    

  
    # View for listing employees
def employee_list(request):
    employees_list = employees.objects.all()
    return render(request, 'employee.html', {'employees_list': employees_list})

    # View for adding a new employee
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})
