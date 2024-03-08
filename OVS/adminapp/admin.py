from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Voter 

class VoterAdmin(UserAdmin):
    list_display = ('id', 'username', 'vote' , 'is_voted')
    search_fields = ('username', 'email', 'first_name', 'last_name','vote','is_voted' )
    list_filter = ('vote', 'gender')
    
    fieldsets = (
            (None, {'fields': ('username', 'password')}),
            ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
            ('Verification Info', {'fields': ('date_of_birth', 'aadhar_number', 'voter_id')}),
            ('Voting Info', {'fields': ('vote', 'is_voted')}),
        )

admin.site.register(Voter,VoterAdmin)

# admin.site.register(Voter)