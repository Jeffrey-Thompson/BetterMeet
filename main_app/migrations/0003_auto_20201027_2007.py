# Generated by Django 3.1.2 on 2020-10-27 20:07

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_preferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='body_type',
            field=models.CharField(choices=[('Slim', 'Slim and Slender'), ('Fit', 'Athletic and Fit'), ('Average', 'Average'), ('Muscular', 'Muscular'), ('Curvy', 'Curvy'), ('Extra', 'A Few Extra Pounds'), ('Heavy', 'Heavyset')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(null=True, verbose_name='Describe yourself in your own words'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='drinks',
            field=models.BooleanField(default=False, verbose_name='I drink alcohol'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('HS', 'High School'), ('college', 'Some College'), ('associate', 'Associates degree'), ('bachelor', 'Bachelors degree'), ('graduate', 'Graduate degree'), ('phd', 'PhD or Post Doctoral')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='has_kids',
            field=models.BooleanField(default=False, verbose_name='I currently have children'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.IntegerField(null=True, verbose_name='Height in centimeters'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='main_app/static/assets'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('tv', 'Watching TV'), ('concert', 'Concerts'), ('cook', 'Cooking'), ('dance', 'Dancing'), ('dine', 'Dining Out'), ('games', 'Video Games'), ('garden', 'Gardening'), ('hike', 'Hiking'), ('movies', 'Movies'), ('art', 'Art'), ('music', 'Music'), ('nightlife', 'Nightlife'), ('playSport', 'Playing Sports'), ('watchSport', 'Watching Sports'), ('reading', 'Reading'), ('religion', 'Religion'), ('shopping', 'Shopping'), ('travel', 'Travel'), ('volunteering', 'Volunteering'), ('gym', 'Working Out')], max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='race',
            field=models.CharField(choices=[('white', 'White'), ('black', 'Black'), ('hispanic', 'Hispanic'), ('asian', 'Asian'), ('native', 'Native American'), ('mideast', 'Middle Eastern'), ('pacific', 'Pacific Islander'), ('indian', 'East Indian'), ('other', 'Other')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relationship_status',
            field=models.CharField(choices=[('single', 'Never Married'), ('married', 'Married'), ('seperated', 'Currently Seperated'), ('divorced', 'Divorced'), ('widow', 'Widow or Widower')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(choices=[('christian', 'Christian'), ('islam', 'Islam'), ('buddist', 'Buddist'), ('hindu', 'Hindu'), ('jewish', 'Jewish'), ('agnostic', 'Agnostic'), ('atheist', 'Atheist'), ('other', 'Other')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex_drive',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='smokes',
            field=models.BooleanField(default=False, verbose_name='I use tobacco'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wants_kids',
            field=models.BooleanField(default=False, verbose_name='I want children in the future'),
        ),
    ]
