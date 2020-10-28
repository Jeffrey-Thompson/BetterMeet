from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from cloudinary.forms import CloudinaryFileField

class User_Form(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['height', 'race', 'body_type', 'relationship_status', 'religion', 'education', 'has_kids', 'wants_kids', 'smokes', 'drinks']

class Image_Upload_Form(ModelForm):
    image = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 400,
            'height': 400,
            'folder': 'images'
        }
    )
    class Meta:
        model = Profile
        fields = ('image',)