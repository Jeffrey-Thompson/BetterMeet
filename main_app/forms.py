from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Message
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field


class User_Form(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
    




class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'height', 'race', 'body_type', 'relationship_status', 'religion', 'education', 'has_kids', 'wants_kids', 'smokes', 'drinks']

class Message_Form(ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'body']