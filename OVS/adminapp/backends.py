# adminapp/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import Voter

class CustomVoterBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Voter.objects.get(username=username,password=password)
        except Voter.DoesNotExist:
            return None

        return None
