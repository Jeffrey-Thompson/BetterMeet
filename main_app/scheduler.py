from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Profile

def update_credits():
    profiles = Profile.objects.all()
    for profile in profiles:
        print(f'changing credits {profile}')
        profile.message_credits = 100
        profile.save()

def start():
    print('starting scheduled task')
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_credits, 'interval', minutes=1440)
    scheduler.start()



