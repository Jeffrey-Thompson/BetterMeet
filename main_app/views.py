from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import User_Form

# Create your views here.

# HOME
def home(request):
    return render (request, 'home.html', {'title': 'BetterMeet'})

# Sign-up
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up- Please try again'
    form = User_Form()
    context = {
        'form': form,
        'error_message': error_message,
        'title': 'User Creation'
    }
    return render(request, 'registration/signup.html', context)
