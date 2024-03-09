# OVS/views.py
from django.shortcuts import render

def HomePage(request):
    return render(request, 'index.html')

def LoginPage(request):
    return render(request, 'login.html')

def RegisterPage(request):
    return render(request, 'register.html')

def AdminPage(request):
    return render(request, 'admin.html')

def VotingPage(request):
    candis = [
        {'name': 'Candidate 1', 'id': 1},
        {'name': 'Candidate 2', 'id': 2},
        {'name': 'Candidate 3', 'id': 3},
    ]
    return render(request, 'vote.html', {'candidates': candis}) 