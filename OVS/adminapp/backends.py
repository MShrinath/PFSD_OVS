# your_app/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile

class CustomUserProfileBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username,password=password)
        except UserProfile.DoesNotExist:
            return None

        return None
