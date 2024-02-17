from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_check, name='registerCheck'),
    path('login/', views.login_check, name='loginCheck'),
    path('logout/', views.logout_the_page, name='logoutPage'),
    # path('vote/', views.vote_check, name='voteCheck'),
]
