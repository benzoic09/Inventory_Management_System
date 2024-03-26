from django import forms
from .models import devicetype, Devices

class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = devicetype
        fields = ['model', 'type', 'status']  # Specify the fields from the devicetype model that you want to include in the form


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Devices 
        fields = ['MacAddress','SerialNo','MobileNo','Model','Cover','status' ]