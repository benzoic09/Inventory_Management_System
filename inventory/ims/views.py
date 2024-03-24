from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import devicetype, devices, employees

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