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

class Message(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipient')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_created']

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

class Utils(models.Model):
    def compareMatch(profile_one, profile_two):
        category_match = 0
        if profile_one.height >= profile_two.preferences.min_height and profile_one.height <= profile_two.preferences.max_height:
            category_match += 1
        if profile_one.sex_drive >= profile_two.preferences.min_sex_drive and profile_one.sex_drive <= profile_two.preferences.max_sex_drive:
            category_match += 1
        if profile_one.has_kids:
            if profile_two.preferences.has_kids:
                category_match += 1
        else:
            if profile_two.preferences.has_no_kids:
                category_match += 1
        if profile_one.wants_kids:
            if profile_two.preferences.wants_kids:
                category_match += 1
        else:
            if profile_two.preferences.never_wants_kids:
                category_match += 1
        if profile_one.smokes:
            if profile_two.preferences.smoke:
                category_match += 1
        else:
            if profile_two.preferences.never_smoke:
                category_match += 1
        if profile_one.drinks:
            if profile_two.preferences.drink:
                category_match += 1
        else:
            if profile_two.preferences.never_drink:
                category_match += 1
        for race in profile_two.preferences.race:
            if profile_one.race == race:
                category_match += 1
        for body_type in profile_two.preferences.body_type:
            if profile_one.body_type == body_type:
                category_match += 1
        for relationship_status in profile_two.preferences.relationship_status:
            if profile_one.relationship_status == relationship_status:
                category_match += 1
        for education in profile_two.preferences.education:
            if profile_one.education == education:
                category_match += 1
        for religion in profile_two.preferences.religion:
            if profile_one.religion == religion:
                category_match += 1
        return category_match

    def common_interests(interests_one, interests_two):
        interest_list = []
        for user_interest in interests_one:
            for match_interest in interests_two:
                if user_interest == match_interest:
                    interest_list.append(user_interest)
        return interest_list

    def match_rating(categories, interests):
        rating = categories * 3
        num_interests = len(interests)
        if num_interests == 0:
            rating = rating - 5
        elif num_interests < 3:
            rating = rating
        elif num_interests < 7:
            rating = rating + 3
        elif num_interests < 10:
            rating = rating + 6
        elif num_interests < 15:
            rating = rating + 10
        elif num_interests < 17:
            rating = rating + 15
        else:
            rating = rating + 17
        if rating < 10:
            score = "Awful"
        elif rating < 20:
            score = "Poor"
        elif rating < 30:
            score = "Average"
        elif rating < 40:
            score = "Good"
        else:
            score = "Great"
        return score