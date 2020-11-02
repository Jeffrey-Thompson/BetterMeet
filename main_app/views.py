from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import User_Form, Profile_Form, Message_Form
from django.contrib.auth.models import User
from .models import Profile, Preferences, Utils, Message
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

# HOME
def home(request):
    return render (request, 'home.html', {'title': 'BetterMeet'})

# Sign-up
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signup_two')
        else:
            error_message = 'Invalid sign up- Please try again'
    form = User_Form()
    context = {
        'form': form,
        'error_message': error_message,
        'title': 'User Creation'
    }
    return render(request, 'registration/signup.html', context)

@login_required
def signup_two(request):
    error_message = ''
    user = request.user
    genders = Profile.objects.order_by().values('gender').distinct()
    if request.method == 'POST':
        sex_drive = request.POST.get('sex_drive')
        gender = request.POST.get('gender')
        gender_custom = request.POST.get('gender_custom')
        description = request.POST.get('description')
        interests = request.POST.get('interests')
        print(interests)
        profile_form = Profile_Form(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.user = user
            if gender_custom:
                new_profile.gender = gender_custom
            else:
                new_profile.gender = gender
            new_profile.sex_drive = sex_drive
            new_profile.description = description
            new_profile.interests = interests.split(',')
            print(new_profile)
            new_profile.save()
            return redirect('signup_three')
        else:
            error_message = "Something isn't right. Please check all fields and try again."
    profile_form = Profile_Form()
    context = {
        'profile_form': profile_form, 
        'error_message': error_message,
        'genders': genders
    }
    return render(request, 'registration/signup_two.html', context)

@login_required
def signup_three(request):
    error_message = ''
    user = request.user
    genders = Profile.objects.order_by().values('gender').distinct()
    if request.method == 'POST':
        max_height = request.POST.get('max_height')
        min_height = request.POST.get('min_height')
        min_sex_drive = request.POST.get('min_sex_drive')
        max_sex_drive = request.POST.get('max_sex_drive')
        genders = request.POST.get('genders')
        body_type = request.POST.get('body_type')
        relationship_status = request.POST.get('relationship_status')
        education = request.POST.get('education')
        religion = request.POST.get('religion')
        race = request.POST.get('race')
        smoke = request.POST.get('smoke')
        if not smoke:
            smoke = False
        never_smoke = request.POST.get('never_smoke')
        if not never_smoke:
            never_smoke = False
        drink = request.POST.get('drink')
        if not drink:
            drink = False
        never_drink = request.POST.get('never_drink')
        if not never_drink:
            never_drink = False
        has_kids = request.POST.get('has_kids')
        if not has_kids:
            has_kids = False
        has_no_kids = request.POST.get('has_no_kids')
        if not has_no_kids:
            has_no_kids = False
        wants_kids = request.POST.get('wants_kids')
        if not wants_kids:
            wants_kids = False
        never_wants_kids = request.POST.get('never_wants_kids')
        if not never_wants_kids:
            never_wants_kids = False
        new_preferences = Preferences(
            profile = user.profile,
            max_height = max_height,
            min_height = min_height,
            min_sex_drive = min_sex_drive,
            max_sex_drive = max_sex_drive,
            smoke = smoke,
            never_smoke = never_smoke,
            drink = drink,
            has_kids = has_kids,
            has_no_kids = has_no_kids,
            wants_kids = wants_kids,
            never_wants_kids = never_wants_kids,
        )
        new_preferences.genders = genders.split(',')
        new_preferences.body_type = body_type.split(',')
        new_preferences.relationship_status = relationship_status.split(',')
        new_preferences.education = education.split(',')
        new_preferences.religion = religion.split(',')
        new_preferences.race = race.split(',')
        new_preferences.save()
        return redirect ('profile_show', profile_id=user.profile.id)
    context = { 
        'error_message': error_message,
        'genders': genders
    }
    return render(request, 'registration/signup_three.html', context)

# Profiles
@login_required
def profile_show(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    user = profile.user
    preferences = profile.preferences
    current_user = request.user
    category_match = Utils.compareMatch(current_user.profile, profile)
    common_interests = Utils.common_interests(current_user.profile.interests, profile.interests)
    match_rating = Utils.match_rating(category_match, common_interests)
    messages = Message.objects.filter(recipient_id=profile_id)[:5]
    context = {
        'profile': profile,
        'user': user,
        'preferences': preferences,
        'title': f"{user.username}'s Profile",
        'category_match': category_match,
        'common_interests': common_interests,
        'match_rating': match_rating,
        'messages': messages,
    }
    return render(request, 'profiles/profile_show.html', context)

#Profile index
@login_required
def profile_index(request):
    user = request.user
    gender_preference = user.profile.preferences.genders
    profiles = Profile.objects.all()
    gender_matches = []
    for profile in profiles:
        if profile.id == user.profile.id:
            continue
        for gender in gender_preference:
            if gender == profile.gender:
                gender_matches.append(profile)
    sexuality_match = []
    for match in gender_matches:
        for gender in match.preferences.genders:
            if gender == user.profile.gender:
                sexuality_match.append(match)
    context = {
        'matches': sexuality_match,
        'title': f"{user.username}'s Matches",
        'user': user
    }
    return render(request, 'profiles/profile_index.html', context)

# Profile Edit
@login_required
def profile_edit(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    genders = Profile.objects.order_by().values('gender').distinct()
    if request.method == 'POST':
        if request.user.id == profile.user.id:
            sex_drive = request.POST.get('sex_drive')
            gender = request.POST.get('gender')
            gender_custom = request.POST.get('gender_custom')
            description = request.POST.get('description')
            interests = request.POST.get('interests')
            print(interests)
            profile_form = Profile_Form(request.POST, instance=profile)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                if gender_custom:
                    profile.gender = gender_custom
                else:
                    profile.gender = gender
                profile.sex_drive = sex_drive
                profile.description = description
                profile.interests = interests.split(',')
                print(profile)
                profile.save()
                return redirect('profile_show', profile_id=profile.id)
    profile_form = Profile_Form(instance=profile)
    interests = ['Watching TV', 'Concerts', 'Dancing', 'Video Games', 'Gardening', 'Travel', 'Cooking', 'Hiking', 'Movies', 'Art', 'Music', 'Nightlife', 'Volunteering', 'Camping', 'Playing Sports', 'Watching Sports', 'Reading', 'Religion', 'Shopping', 'Working Out', 'Board Games']
    context = {
        'title': 'Edit my profile',
        'genders': genders,
        'profile': profile,
        'profile_form': profile_form,
        'interests': interests
    }
    return render(request, 'profiles/profile_edit.html', context)

# Preference Edit
@login_required
def preference_edit(request, preference_id):
    genders = Profile.objects.order_by().values('gender').distinct()
    preferences = Preferences.objects.get(id=preference_id)
    races = ['White', 'Black', 'Pacific Islander', 'Asian', 'Native American', 'Middle Eastern', 'Hispanic', 'East Indian', 'Other']
    body_types = ['Slim and Slender', 'Athletic and Fit', 'Average', 'Muscular', 'Curvy', 'A Few Extra Pounds', 'Heavyset']
    relationship_statuses = ['Never Married', 'Married', 'Currently Seperated', 'Divorced', 'Widow or Widower']
    educations = ['High School', 'Some College', 'Associates degree', 'Bachelors degree', 'Graduate degree', 'PhD or Post Doctoral']
    religions = ['Christian', 'Islam', 'Buddist', 'Hindu', 'Jewish', 'Agnostic', 'Atheist', 'Other']
    if request.method == 'POST':
        if request.user.id == preferences.profile.user.id:
            max_height = request.POST.get('max_height')
            min_height = request.POST.get('min_height')
            min_sex_drive = request.POST.get('min_sex_drive')
            max_sex_drive = request.POST.get('max_sex_drive')
            genders = request.POST.get('genders')
            body_type = request.POST.get('body_type')
            relationship_status = request.POST.get('relationship_status')
            education = request.POST.get('education')
            religion = request.POST.get('religion')
            race = request.POST.get('race')
            smoke = request.POST.get('smoke')
            if not smoke:
                smoke = False
            never_smoke = request.POST.get('never_smoke')
            if not never_smoke:
                never_smoke = False
            drink = request.POST.get('drink')
            if not drink:
                drink = False
            never_drink = request.POST.get('never_drink')
            if not never_drink:
                never_drink = False
            has_kids = request.POST.get('has_kids')
            if not has_kids:
                has_kids = False
            has_no_kids = request.POST.get('has_no_kids')
            if not has_no_kids:
                has_no_kids = False
            wants_kids = request.POST.get('wants_kids')
            if not wants_kids:
                wants_kids = False
            never_wants_kids = request.POST.get('never_wants_kids')
            if not never_wants_kids:
                never_wants_kids = False
            
            preferences.max_height = max_height
            preferences.min_height = min_height
            preferences.min_sex_drive = min_sex_drive
            preferences.max_sex_drive = max_sex_drive
            preferences.smoke = smoke
            preferences.never_smoke = never_smoke
            preferences.drink = drink
            preferences.has_kids = has_kids
            preferences.has_no_kids = has_no_kids
            preferences.wants_kids = wants_kids
            preferences.never_wants_kids = never_wants_kids
            
            preferences.genders = genders.split(',')
            preferences.body_type = body_type.split(',')
            preferences.relationship_status = relationship_status.split(',')
            preferences.education = education.split(',')
            preferences.religion = religion.split(',')
            preferences.race = race.split(',')
            preferences.save()
        return redirect ('profile_show', profile_id=preferences.profile.id)
    context = {
        'title': 'Edit my preferences',
        'genders': genders,
        'preferences': preferences,
        'races': races,
        'body_types': body_types,
        'relationship_statuses': relationship_statuses,
        'educations': educations,
        'religions': religions
    }
    return render(request, 'profiles/preferences_edit.html', context)

# User Delete
@login_required
def user_delete(request, user_id):
    if request.user.id == user_id:
        User.objects.get(id=user_id).delete()
        return redirect('home')

# Create Message
@login_required
def create_message(request, recipient_id):
    recipient = Profile.objects.get(id=recipient_id)
    current_user = request.user
    category_match = Utils.compareMatch(current_user.profile, recipient)
    common_interests = Utils.common_interests(current_user.profile.interests, recipient.interests)
    match_rating = Utils.match_rating(category_match, common_interests)
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        sender = request.user.profile
        recipient = recipient
        Message.objects.create(title=title, body=body, sender=sender, recipient=recipient)
        return redirect('profile_index')
    context = {
        'title': 'Send Message',
        'profile': recipient,
        'common_interests': common_interests,
        'match_rating': match_rating,
    }
    return render(request, 'messages/create.html', context)

#All Messages
@login_required
def messages_all(request):
    user = request.user
    messages = Message.objects.filter(Q(sender_id=user.profile.id) | Q(recipient_id=user.profile.id))
    context = {
        'title': 'Message Center',
        'messages': messages,
        'user': user,
    }
    return render(request, 'messages/all.html', context)
