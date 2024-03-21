from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render (request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index.html')  # Replace 'home' with your desired URL name
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'login_form': form})