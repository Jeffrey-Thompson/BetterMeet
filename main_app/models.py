from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


# Create your models here.
body_type_choices = [  
    ('Slim', 'Slim and Slender'),
    ('Fit', 'Athletic and Fit'),
    ('Average', 'Average'),
    ('Muscular', 'Muscular'),
    ('Curvy', 'Curvy'),
    ('Extra', 'A Few Extra Pounds'),
    ('Heavy', 'Heavyset'),
]

relationship_choices = [
    ('single', 'Never Married'),
    ('married', 'Married'),
    ('seperated', 'Currently Seperated'),
    ('divorced', 'Divorced'),
    ('widow', 'Widow or Widower'),
]

education_choices = [
    ('HS', 'High School'),
    ('college', 'Some College'),
    ('associate', 'Associates degree'),
    ('bachelor', 'Bachelors degree'),
    ('graduate', 'Graduate degree'),
    ('phd', 'PhD or Post Doctoral')
]

religion_choices = [
    ('christian', 'Christian'),
    ('islam', 'Islam'),
    ('buddist', 'Buddist'),
    ('hindu', 'Hindu'),
    ('jewish', 'Jewish'),
    ('agnostic', 'Agnostic'),
    ('atheist', 'Atheist'),
    ('other', 'Other'),
]

race_choices = [
    ('white', 'White'),
    ('black', 'Black'),
    ('hispanic', 'Hispanic'),
    ('asian', 'Asian'),
    ('native', 'Native American'),
    ('mideast', 'Middle Eastern'),
    ('pacific', 'Pacific Islander'),
    ('indian', 'East Indian'),
    ('other', 'Other'),
]

intereset_choices = [
    ('tv', 'Watching TV'),
    ('concert', 'Concerts'),
    ('cook', 'Cooking'),
    ('dance', 'Dancing'),
    ('dine', 'Dining Out'),
    ('games', 'Video Games'),
    ('garden', 'Gardening'),
    ('hike', 'Hiking'),
    ('movies', 'Movies'),
    ('art', 'Art'),
    ('music', 'Music'),
    ('nightlife', 'Nightlife'),
    ('playSport', 'Playing Sports'),
    ('watchSport', 'Watching Sports'),
    ('reading', 'Reading'),
    ('religion', 'Religion'),
    ('shopping', 'Shopping'),
    ('travel', 'Travel'),
    ('volunteering', 'Volunteering'),
    ('gym', 'Working Out')
]

class Profile(models.Model):


    image = models.URLField('Link to a picture of you')
    message_credits = models.IntegerField(default=100)
    height = models.IntegerField('Height in centimeters', null=True)
    sex_drive = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    gender = models.CharField(max_length=200, null=True)
    body_type = models.CharField(max_length=200, choices=body_type_choices, null=True)
    relationship_status = models.CharField(max_length=200, choices=relationship_choices, null=True)
    education = models.CharField(max_length=200, choices=education_choices, null=True)
    religion = models.CharField(max_length=200, choices=religion_choices, null=True)
    race = models.CharField(max_length=200, choices=race_choices, null=True)
    interests = ArrayField(models.CharField(max_length=200, choices=intereset_choices))
    description = models.TextField('Describe yourself in your own words', null=True)
    has_kids = models.BooleanField('I currently have children', default=False)
    wants_kids = models.BooleanField('I want children in the future', default=False)
    smokes = models.BooleanField('I use tobacco', default=False)
    drinks = models.BooleanField('I drink alcohol', default=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.user.username} Profile')


class Preferences(models.Model):
    
    max_height = models.IntegerField()
    min_height = models.IntegerField(validators=[MinValueValidator(0)])
    min_sex_drive = models.IntegerField(validators=[MinValueValidator(0)])
    max_sex_drive = models.IntegerField(validators=[MaxValueValidator(100)])
    genders = ArrayField(models.CharField(max_length=200))
    body_type = ArrayField(models.CharField(max_length=200, choices=body_type_choices))
    relationship_status = ArrayField(models.CharField(max_length=200, choices=relationship_choices))
    education = ArrayField(models.CharField(max_length=200, choices=education_choices))
    religion = ArrayField(models.CharField(max_length=200, choices=religion_choices))
    race = ArrayField(models.CharField(max_length=200, choices=race_choices))
    smoke = ArrayField(models.BooleanField())
    drink = ArrayField(models.BooleanField())
    has_kids = ArrayField(models.BooleanField())
    wants_kids = ArrayField(models.BooleanField())

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.profile.user.username} preferences')