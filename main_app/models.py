from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


# Create your models here.
body_type_choices = [  
    ('Slim and Slender', 'Slim and Slender'),
    ('Athletic and Fit', 'Athletic and Fit'),
    ('Average', 'Average'),
    ('Muscular', 'Muscular'),
    ('Curvy', 'Curvy'),
    ('A Few Extra Pounds', 'A Few Extra Pounds'),
    ('Heavyset', 'Heavyset'),
]

relationship_choices = [
    ('Never Married', 'Never Married'),
    ('Married', 'Married'),
    ('Currently Seperated', 'Currently Seperated'),
    ('Divorced', 'Divorced'),
    ('Widow or Widower', 'Widow or Widower'),
]

education_choices = [
    ('High School', 'High School'),
    ('Some College', 'Some College'),
    ('Associates degree', 'Associates degree'),
    ('Bachelors degree', 'Bachelors degree'),
    ('Graduate degree', 'Graduate degree'),
    ('PhD or Post Doctoral', 'PhD or Post Doctoral')
]

religion_choices = [
    ('Christian', 'Christian'),
    ('Islam', 'Islam'),
    ('Buddist', 'Buddist'),
    ('Hindu', 'Hindu'),
    ('Jewish', 'Jewish'),
    ('Agnostic', 'Agnostic'),
    ('Atheist', 'Atheist'),
    ('Other', 'Other'),
]

race_choices = [
    ('White', 'White'),
    ('Black', 'Black'),
    ('Hispanic', 'Hispanic'),
    ('Asian', 'Asian'),
    ('Native', 'Native American'),
    ('Middle Eastern', 'Middle Eastern'),
    ('Pacific Islander', 'Pacific Islander'),
    ('East Indian', 'East Indian'),
    ('Other', 'Other'),
]

intereset_choices = [
    ('Watching TV', 'Watching TV'),
    ('Concerts', 'Concerts'),
    ('Cooking', 'Cooking'),
    ('Dancing', 'Dancing'),
    ('Dining Out', 'Dining Out'),
    ('Video Games', 'Video Games'),
    ('Gardening', 'Gardening'),
    ('Hiking', 'Hiking'),
    ('Movies', 'Movies'),
    ('Art', 'Art'),
    ('Music', 'Music'),
    ('Nightlife', 'Nightlife'),
    ('Playing Sports', 'Playing Sports'),
    ('Watching Sports', 'Watching Sports'),
    ('Reading', 'Reading'),
    ('Religion', 'Religion'),
    ('Shopping', 'Shopping'),
    ('Travel', 'Travel'),
    ('Volunteering', 'Volunteering'),
    ('Working Out', 'Working Out'),
    ('Camping', 'Camping'),
    ('Board Games', 'Board Games')
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
    interests = ArrayField(models.CharField(max_length=200, choices=intereset_choices),default=list)
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
    smoke = models.BooleanField(default=False)
    never_smoke = models.BooleanField(default=False)
    drink = models.BooleanField(default=False)
    never_drink = models.BooleanField(default=False)
    has_kids = models.BooleanField(default=False)
    has_no_kids = models.BooleanField(default=False)
    wants_kids = models.BooleanField(default=False)
    never_wants_kids = models.BooleanField(default=False)

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.profile.user.username} preferences')