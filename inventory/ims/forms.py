from django import forms
from .models import devicetype, Devices, employees, Assignment

class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = devicetype
        fields = ['model', 'type', 'status']  # Specify the fields from the devicetype model that you want to include in the form


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Devices 
        fields = ['MacAddress','SerialNo','MobileNo','Model','Cover','status' ]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model =  employees
        fields = ['empno','Name','Department','branch']


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['user','device']