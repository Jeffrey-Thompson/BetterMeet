from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User_Form(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')