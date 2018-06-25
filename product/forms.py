from django import forms
from django.contrib.auth.models import User
from .models import Product, Producent



class FiltrCotojestForm(forms.ModelForm):
	
	class Meta:
		model = Product
		fields = ('cotojest',)
		

class FiltrRynekForm(forms.Form):
	RYNEK_CHOICES = (('1', 'wtórny'), 
						('2', 'pierwotny'))
	rynek = forms.ChoiceField(choices=RYNEK_CHOICES, label='Rynek')
		


