from django import forms
from django.contrib.auth.models import User
from .models import Klient, Lokacja


class KlientEditForm(forms.ModelForm):
	class Meta:
		model = Klient
		fields = ('nazwa', 
					'firma', 
					'miejscowosc', 
					'adres', 
					'kodpocztowy', 
					'rodzfirm', 
					'nip', 
					'krs', 
					'ceidg', 
					'regon', 
					'shortopis', 
					'opis', 
					'link2')
		

class SprFirm(forms.Form):
	nip_firmy = forms.CharField(max_length=10)

	
class LokacjaEditForm(forms.ModelForm):
	class Meta:
		model = Lokacja
		fields = ('nazwa', 
					'miejscowosc', 
					'adres', 
					'kodpocztowy', 
					'dzienodciecia', 
					'dnidostawy', 
					'godzdostawy', 
					'shortopis')
	
	
'''class ImageItemEditForm(forms.ModelForm):
	class Meta:
		model = ImageItem
		fields = ('title', 'image', 'opis')	'''