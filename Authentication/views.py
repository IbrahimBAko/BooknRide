from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from Authentication.models import User

# Create your views here.

def register (request):
    if request.method == 'POST':
        form = UserRegisterForm (request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')

            # creating the UserProfile instance but do not save it yet
            profile = profile_form.save(commit=False)
            # profile.user = new_user # Assigning the profile for our newly created user!
            profile.user = new_user
            profile.save() # Now save the UserProfile instance.

            messages.success(request, f'{username}, Your account has been successfully saved')

            # Authenticate with username or email, depending on your authentication backend
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate (request, username=email, password=password)
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
            print(profile_form.errors)

    else :
            form = UserRegisterForm()
            profile_form = ProfileForm()

    context = {
            'form' : form,
            'profile_form' : profile_form
        } 

    return render (request, 'authentication/register.html', context)
