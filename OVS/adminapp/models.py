from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField(blank=True, null=True)
    aadhar_number = models.CharField(max_length=12, blank=True, null=True, unique=True)
    voter_id = models.CharField(max_length=20, blank=True, null=True, unique=True)
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False)
    vote = models.IntegerField (default=-1,blank=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "user_profile"
