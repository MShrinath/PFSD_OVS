# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db import IntegrityError  
from .models import UserProfile

def logout_view(request):
    logout(request)
    return redirect('homePage')

def register_view(request):
    if request.user.is_authenticated:
        return render(request, 'already_loggedin.html')
    if request.method == 'POST':
        try:
            # Extract user input from the form
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

        except IntegrityError as e:
            error_message = "Registration failed. The provided email or username is already registered."
            return render(request, 'register.html', {'error_message': error_message})

        except Exception as e:
            error_message = "An error occurred during registration. Please try again later."
            return render(request, 'register.html', {'error_message': error_message})

    return render(request, 'register.html')


def login_view(request):
    return render(request, 'login.html')