from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Profile(models.Model):

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

    image = models.ImageField()
    message_credits = models.IntegerField(default=100)
    height = models.IntegerField()
    sex_drive = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    gender = models.CharField(max_length=200)
    body_type = models.CharField(max_length=200, choices=body_type_choices)
    relationship_status = models.CharField(max_length=200, choices=relationship_choices)
    education = models.CharField(max_length=200, choices=education_choices)
    religion = models.CharField(max_length=200, choices=religion_choices)
    race = models.CharField(max_length=200, choices=race_choices)
    interests = ArrayField(models.CharField(max_length=200, choices=intereset_choices))
    description = models.TextField()
    has_kids = models.BooleanField()
    wants_kids = models.BooleanField()
    smokes = models.BooleanField()
    drinks = models.BooleanField()

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.user.username} Profile')

class Preferences(models.Model):
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