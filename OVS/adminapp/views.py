# adminapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login , logout
from django.db import IntegrityError  
from .models import UserProfile

def logout_the_page(request):
    logout(request)
    return redirect('homePage')

def register_check(request):
    error_message = None

    if request.method == 'POST':
        try:
            # Extract form data
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            date_of_birth = request.POST['date_of_birth']
            aadhar_number = request.POST['aadhar_number']
            voter_id = request.POST['voter_id']
            gender = request.POST['gender']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']

            # Create a new user profile
            user_profile = UserProfile.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                aadhar_number=aadhar_number,
                voter_id=voter_id,
                gender=gender,
                email=email,
                username=username,
                password=password,
            )
            
            return redirect('homePage')

        except IntegrityError:
            error_message = "Registration failed. The provided email or username is already registered."

        except Exception:
            error_message = "An error occurred during registration. Please try again later."

    return render(request, 'register.html', {'error_message': error_message})

def login_check(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = UserProfile.objects.get(username=username, password=password)
        except UserProfile.DoesNotExist:
            user = None

        if user is not None:
            login(request, user, backend='adminapp.backends.CustomUserProfileBackend')
            return redirect('homePage')
        else:
            error_message = 'Wrong username or password.'

    return render(request, 'login.html', {'error_message': error_message})
