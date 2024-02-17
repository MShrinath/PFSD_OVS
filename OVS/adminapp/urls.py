from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_page, name='logoutPage'),
    path('loginfail/', views.loginfail_view, name='loginfail'),
]
