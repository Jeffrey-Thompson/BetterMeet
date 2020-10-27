from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import User_Form, Profile_Form, Image_Upload_Form
from django.contrib.auth.models import User

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
    instance = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        image_form = Image_Upload_Form(request.POST, request.FILES, instance=instance)
        profile_form = Profile_Form(request.POST)
        print(profile_form)
        print(profile_form.is_valid())
        print(request.body)
        if profile_form.is_valid() and image_form.is_valid():
            image_form.save()
            new_profile = profile_form.save(commit=False)
            new_profile.user = user
            new_profile.save()
            return redirect('home')
        else:
            error_message = "Something isn't right. Please check all fields and try again."
    image_form = Image_Upload_Form()
    profile_form = Profile_Form()
    context = {
        'profile_form': profile_form, 
        'error_message': error_message,
        'image_form': image_form
    }
    return render(request, 'registration/signup_two.html', context)

