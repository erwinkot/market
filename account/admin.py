from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'klient', 'czygrupa', 'status', 'lokacja', 'photo']
	list_filter = ['klient', 'czygrupa', 'status', 'lokacja']
	
admin.site.register(Profile, ProfileAdmin)