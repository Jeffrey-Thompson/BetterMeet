from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('', views.home, name='home'),

    # Sign-up
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/signup_two', views.signup_two, name='signup_two'),
    path('accounts/signup_three', views.signup_three, name='signup_three'),

    # Profile
    path('profiles/<int:profile_id>/edit', views.profile_edit, name="profile_edit"),
    path('profiles/<int:preference_id>/edit_preference', views.preference_edit, name="preference_edit"),
    path('profiles/<int:profile_id>/', views.profile_show, name="profile_show"),
    path('profiles/index/', views.profile_index, name="profile_index"),
]