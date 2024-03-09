# adminapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login , logout
from django.db import IntegrityError  
from .models import Voter

from django.http import JsonResponse

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
            user_profile = Voter.objects.create(
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
            user = Voter.objects.get(username=username, password=password)
        except Voter.DoesNotExist:
            user = None

        if user is not None:
            login(request, user, backend='adminapp.backends.CustomVoterBackend')
            return redirect('votingPage')
        else:
            error_message = 'Wrong username or password.'

    return render(request, 'login.html', {'error_message': error_message})


def logout_the_page(request):
    logout(request)
    return redirect('homePage')

def vote_check(request):

    if request.method == 'POST':
        vote = request.POST['vote']
        voter = request.user
        voter.vote = vote
        voter.is_voted = True
        voter.save()

        return redirect('homePage')

def admin_stats_data(request):
    lbl = ['Not Voted','Candi1','Candi2','Candi3'] 
    votes_query_set = Voter.objects.values_list('vote', flat=True)
    votes_list = list(votes_query_set)
    vote_0 = votes_list.count(0)
    vote_1 = votes_list.count(1)
    vote_2 = votes_list.count(2)
    vote_3 = votes_list.count(3)
    dts = [{'label': 'Voting','data': [vote_0,vote_1,vote_2,vote_3],'backgroundColor': ['#848884','#ec1c24','#fff200','#0ed145' ]}]
    data = {'labels':lbl,'datasets':dts}
    return JsonResponse({
        'type': 'doughnut',
        'data': data,
        })

def admin_stats(request):
    return render(request, 'admin_stats.html',{})