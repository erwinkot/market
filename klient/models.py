from django.core.urlresolvers import reverse
from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from kontrahent.models import Miejscowosc



class Catkli(models.Model):
	nazwa = models.CharField(max_length=60, default='gotówka')
	slug = models.SlugField(max_length=66, blank=True)

	class Meta:
		ordering = ('nazwa',)
		
	def __str__(self):
		return self.nazwa


class Klient(models.Model):
	RODZFIRM_CHOICES = (('działalność', 'Jednoosobowa działalność gospodarcza'), 
							('spółka cywilna', 'Spółka cywilna'),
							('spółka jawna', 'Spółka jawna'),
							('spółka komandytowa', 'Spółka komandytowa'),
							('spółka zoo', 'Spółka z.o.o'),
							('spółka akcyjna', 'Spółka akcyjna'))
	STATUS_CHOICES = (('aktywny', 'aktywny'), ('ban', 'ban'))
	RODZKLI_CHOICES = (('gotówka', 'gotówka'), ('przelew', 'przelew'))
	nazwa = models.CharField(max_length=30, unique=True, blank=True)
	slug = models.SlugField(max_length=50, blank=True)
	firma = models.CharField(max_length=80)
	miejscowosc = models.ForeignKey(Miejscowosc, related_name='klientos', blank=True)
	adres = models.CharField(max_length=60)
	kodpocztowy = models.CharField(max_length=6)
	rodzfirm = models.CharField(max_length=60, choices=RODZFIRM_CHOICES, default='działalność')
	nip = models.CharField(max_length=10)
	krs = models.CharField(max_length=10, blank=True)
	ceidg = models.CharField(max_length=10, blank=True)
	regon = models.CharField(max_length=9, blank=True)
	shortopis = models.CharField(max_length=200, blank=True)
	opis = models.TextField(blank=True)
	link2 = models.URLField(blank=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aktywny')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	rodzplat = models.CharField(max_length=20, choices=RODZKLI_CHOICES, default='gotówka')

	class Meta:
		ordering = ('nazwa',)
		
	def __str__(self):
		return self.nazwa
		
	#def save(self, *args, **kwargs):
		#if not self.slug:
			#self.slug = slugify(self.nazwa)
			#super(Klient, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('klient:editfirm',
							args=[self.nip])
							
						
class Lokacja(models.Model):
	DZIEN_CHOICES = (('poniedziałek', 'poniedziałek'),
						('wtorek', 'wtorek'),
						('środa', 'środa'),
						('czwartek', 'czwartek'),
						('piątek', 'piątek'))
	klient = models.ForeignKey(Klient, related_name='lokacjas')
	nazwa = models.CharField(max_length=40, unique=True, blank=True)
	slug = models.SlugField(max_length=50, blank=True)
	miejscowosc = models.ForeignKey(Miejscowosc, related_name='lokacjas', default=2)
	adres = models.CharField(max_length=60, blank=True)
	kodpocztowy = models.CharField(max_length=6, blank=True)
	dzienodciecia = models.CharField(max_length=15, blank=True, choices=DZIEN_CHOICES)
	dnidostawy = models.CharField(max_length=25, blank=True)
	godzdostawy = models.CharField(max_length=25, blank=True)
	shortopis = models.CharField(max_length=100, blank=True)
	link1 = models.URLField(blank=True)
	link2 = models.URLField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('nazwa',)
		
	def __str__(self):
		return self.nazwa
		
	#def save(self, *args, **kwargs):
		#if not self.slug:
			#self.slug = slugify(self.nazwa)
			#super(Lokacja, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('klient:lokacja',
							args=[self.nazwa])
							
							
							
class Detale(models.Model):
	klient = models.OneToOneField(Klient, related_name='detales')
	rabatz = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
	rabatr = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
	kredytlimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
	peyment = models.PositiveIntegerField(blank=True, default=0)
	
	
class Grupa(models.Model):
	nazwa = models.CharField(max_length=40, db_index=True)
	slug = models.SlugField(max_length=50, blank=True)
	
	class Meta:
		ordering = ('nazwa',)
		
	def __str__(self):
		return self.nazwa
		
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.nazwa)
			super(Grupa, self).save(*args, **kwargs)