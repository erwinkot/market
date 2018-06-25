from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse

class Producent(models.Model):
	nazwa = models.CharField(max_length=30, db_index=True)
	slug = models.SlugField(max_length=40, db_index=True, unique=True)
	firma = models.CharField(max_length=100, blank=True)
	kraj = models.CharField(max_length=60, blank=True)
	miasto = models.CharField(max_length=30, blank=True)
	kodpocztowy = models.CharField(max_length=20, blank=True)
	ulica = models.CharField(max_length=40, blank=True)
	numer = models.CharField(max_length=10, blank=True)
	
	
	class Meta:
		ordering = ('nazwa',)


	def __str__(self):
		return self.nazwa
		
	def get_absolute_url(self):
		return reverse('product:jh_list_by_producent',
							args=[self.slug])
	

	
	
class Profilmat(models.Model):
	nazwa = models.CharField(max_length=30)
	slug = models.SlugField(max_length=40, unique=True)	
	

	class Meta:
		ordering = ('nazwa',)


	def __str__(self):
		return self.nazwa
		
		

class Cotojest(models.Model):
	nazwa = models.CharField(max_length=60, unique=True)
	slug = models.SlugField(max_length=70, unique=True)	
	
	class Meta:
		ordering = ('nazwa',)


	def __str__(self):
		return self.nazwa
		
	def get_absolute_url(self):
		return reverse('product:jh_list_by_producent',
							args=[self.slug])
		
class Product(models.Model):
	
	nazwa = models.CharField(max_length=60, db_index=True)
	slug = models.SlugField(max_length=80, db_index=True, unique=True)
	producent = models.ForeignKey(Producent, related_name='products', blank=True)
	cotojest = models.ForeignKey(Cotojest, related_name='productsy')
	kategoria = models.CharField(max_length=60, blank=True)
	shortopis = models.CharField(max_length=100, blank=True)
	opis = models.TextField(blank=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	fotka = models.URLField(blank=True)
	dokprod1 = models.URLField(blank=True)
	dokprod2 = models.URLField(blank=True)
	dokprod3 = models.URLField(blank=True)
	dokprod4 = models.URLField(blank=True)
	pod_vat = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	profilmat = models.ForeignKey(Profilmat, related_name='productsy')

	class Meta:
		ordering = ('nazwa',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def __str__(self):
		return self.nazwa

	def get_absolute_url(self):
		return reverse('product:jh_list_by_product',
							args=[self.slug])


class Jh(models.Model):
	jh = models.ForeignKey(Product, related_name='jhs')
	name = models.CharField(max_length=80, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	opis1 = models.CharField(max_length=80, blank=True)
	opis2 = models.CharField(max_length=80, blank=True)
	opis3 = models.CharField(max_length=80, blank=True)
	image = models.ImageField(upload_to='jhs/%Y/%m/%d',
							blank=True)
	jm = models.CharField(max_length=8)
	ilop = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
	nrkat = models.CharField(max_length=30, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
	stock = models.PositiveIntegerField(blank=True)
	rabatmax = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
	zawart = models.CharField(max_length=200, blank=True)
	label = models.CharField(max_length=60, blank=True)
	status = models.CharField(max_length=20, blank=True)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product:jh_detail',
						args=[self.id, self.slug])

