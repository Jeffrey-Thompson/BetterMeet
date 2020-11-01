from django.contrib import admin

from .models import Profile, Preferences, Message
# Register your models here.
admin.site.register(Profile)
admin.site.register(Preferences)
admin.site.register(Message)
