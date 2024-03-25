from django import forms
from .models import devicetype

class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = devicetype
        fields = ['model', 'type', 'status']  # Specify the fields from the devicetype model that you want to include in the form
        