from django.shortcuts import render

def HomePage(request):
    return render(request, 'index.html')

def LoginPage(request):
    error_message = request.GET.get('error_message', None)
    return render(request, 'login.html', {'error_message': error_message})

def RegisterPage(request):
    return render(request, 'register.html')

def AdminPage(request):
    return render(request, 'admin.html')

def VotingPage(request):
    return render(request, 'vote.html') 