from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

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

    interset_choices = [
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
    message_credits = models.IntergerField(default=100)
    height = models.IntegerField()
    sex_drive = models.IntegerField(min_value=0, max_value=100)
    gender = models.CharField()
    body_type = models.CharField(choices=body_type_choices)
    relationship_status = models.CharField(choices=relationship_choices)
    education = models.CharField(choices=education_choices)
    religion = models.CharField(choices=religion_choices)
    race = models.CharField(choices=race_choices)
    interests = ArrayField(models.CharField(choices=interset_choices))
    description = models.TextField()
    has_kids = models.BooleanField()
    wants_kids = models.BooleanField()
    smokes = models.BooleanField()
    drinks = models.BooleanField()