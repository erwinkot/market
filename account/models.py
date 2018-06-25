from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from klient.models import Klient, Grupa

class Profile(models.Model):
	STATUS_CHOICES = (('uprawniony', 'Uprawniony'), ('zamawiający', 'Zamawiający'))
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	klient = models.ForeignKey(Klient, related_name='profiles', default=1)
	czygrupa = models.CharField(max_length=30, default='indywidualny')
	status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='zamawiający')
	photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
	lokacja = models.CharField(max_length=30, blank=True)
	kodupraw = models.CharField(max_length=30, blank=True)
	activgrup = models.BooleanField(default=False)
	grupa = models.ForeignKey(Grupa, related_name='profiles', default=1)
						  