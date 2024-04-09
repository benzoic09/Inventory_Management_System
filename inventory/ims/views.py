from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import devicetype, Devices, employees, Assignment
from .forms import DeviceTypeForm, DeviceForm, EmployeeForm, AssignmentForm

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
    assignments = Assignment.objects.all()
    #Count allocated devices
    allocated_devices_count  = assignments.count()
    #create device obj and count devices
    device_count = Devices.objects.all()
    device_list_count = device_count.count
    # create and count empoyees
    employees_list = employees.objects.all()
    empcount = employees_list.count()
     # Pass count and queryset to template context
    context= {
        'allocated_devices_count':allocated_devices_count, 'assignments':assignments,
        'device_list_count':device_list_count, 'empcount':empcount}
    return render(request, 'home.html', context)

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


   # View for Assignment
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AssignmentForm()
    return render(request, 'add_assignment.html', {'form': form})
