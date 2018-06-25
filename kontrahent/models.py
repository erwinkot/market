from django.core.urlresolvers import reverse
from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify


class Wojewodztwo(models.Model):					
	nazwa = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True)
	wojewoda = models.CharField(max_length=50, blank=True)
						
	class Meta:
		ordering = ('nazwa',)
	
	def __str__(self):
			return self.nazwa	
			
			
class Powiat(models.Model):					
	nazwa = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True)
	starosta = models.CharField(max_length=50, blank=True)
	wojewodztwo = models.ForeignKey(Wojewodztwo, related_name='powiatos')
						
	class Meta:
		ordering = ('nazwa',)
	
	def __str__(self):
			return self.nazwa


class Gmina(models.Model):					
	nazwa = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True)
	wojt = models.CharField(max_length=50, blank=True)
	powiat = models.ForeignKey(Powiat, related_name='gminas')
						
	class Meta:
		ordering = ('nazwa',)
	
	def __str__(self):
			return self.nazwa			
			
class Miejscowosc(models.Model):
	MIASTO_CHOICES = (('miasto', 'Miasto'), ('wieś', 'Wieś'))
	nazwa = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True)
	profil = models.CharField(max_length=30, choices=MIASTO_CHOICES, default='miasto')
	gmina = models.ForeignKey(Gmina, related_name='miejscowosci')
	
	class Meta:
		ordering = ('nazwa',)
	
	def __str__(self):
			return self.nazwa