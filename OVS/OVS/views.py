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
    return render(request, 'vote.html') 