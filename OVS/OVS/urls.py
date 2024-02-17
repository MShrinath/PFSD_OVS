# OVS/urls.py
from django.contrib import admin
from django.urls import path ,include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage,name='homePage'),
    path('login', views.LoginPage,name='loginPage'),
    path('register', views.RegisterPage,name='registerPage'),
    path('vote',views.VotingPage,name='votingPage'),
    path('', include('adminapp.urls')),
]
