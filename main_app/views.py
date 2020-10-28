from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import User_Form, Profile_Form
from django.contrib.auth.models import User
from .models import Profile

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
            return redirect('signup_two')
        else:
            error_message = 'Invalid sign up- Please try again'
    form = User_Form()
    context = {
        'form': form,
        'error_message': error_message,
        'title': 'User Creation'
    }
    return render(request, 'registration/signup.html', context)

def signup_two(request):
    error_message = ''
    user = request.user
    genders = Profile.objects.order_by().values('gender').distinct()
    if request.method == 'POST':
        sex_drive = request.POST.get('sex_drive')
        gender = request.POST.get('gender')
        gender_custom = request.POST.get('gender_custom')
        description = request.POST.get('description')
        profile_form = Profile_Form(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.user = user
            if gender_custom:
                new_profile.gender = gender_custom
            else:
                new_profile.gender = gender
            new_profile.sex_drive = sex_drive
            new_profile.description = description
            print(new_profile)
            new_profile.save()
            return redirect('home')
        else:
            error_message = "Something isn't right. Please check all fields and try again."
    profile_form = Profile_Form()
    context = {
        'profile_form': profile_form, 
        'error_message': error_message,
        'genders': genders
    }
    return render(request, 'registration/signup_two.html', context)

