from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('', views.home, name='home'),

    # Sign-up
    path('accounts/signup', views.signup, name='signup'),
]