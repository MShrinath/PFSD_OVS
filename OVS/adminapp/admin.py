from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Voter 

class VoterAdmin(UserAdmin):
    list_display = ('id', 'username', 'vote' , 'is_voted')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('vote', 'gender')

admin.site.register(Voter,VoterAdmin)

# admin.site.register(Voter)