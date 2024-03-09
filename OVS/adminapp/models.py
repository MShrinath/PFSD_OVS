# adminapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Voter(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    aadhar_number = models.CharField(max_length=12, blank=True, null=True, unique=True)
    voter_id = models.CharField(max_length=20, blank=True, null=True, unique=True)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    VOTE_CHOICES = [
        (0, 'Not Voted'),
        (1, 'Candidate 1'),
        (2, 'Candidate 2'),
        (3, 'Candidate 3'),
    ]
    vote = models.IntegerField(default=0, choices=VOTE_CHOICES)
    is_voted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.get_full_name()

    class Meta:
        db_table = "voter"
