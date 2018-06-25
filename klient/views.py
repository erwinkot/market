from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import KlientEditForm, SprFirm, LokacjaEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Klient, Lokacja
from account.models import Profile
from django.contrib.auth.models import User


@login_required
def potw_nip(request):
		
	return render(request, 'klient/potw_nip.html',)	

@login_required
def firma_sprawdzana(request, nip=None):
	
	if request.method == 'POST':
		spr_form = SprFirm(request.POST)
		if spr_form.is_valid():
			cd = spr_form.cleaned_data
			klient = Klient.objects.filter(nip=cd['nip_firmy'])
			if klient:
				klient = get_object_or_404(Klient, nip=cd['nip_firmy'])
				profile = get_object_or_404(Profile, user=request.user)
				profile.klient = klient
				profile.save()
				
			
				return render(request, 'klient/sprfirma.html', {'klient': klient})
			
			else: 	
				komenda = 'Firma o podanym NIP-ie nie istnieje.'
				return render(request, 'klient/sprfirma.html', {'komenda': komenda})
	else:
		spr_form = SprFirm()
		
	return render(request, 'klient/sprfirma.html', {'spr_form': spr_form})
	
	
	
@login_required
def new_firm(request): 
	
	if request.method == 'POST':
		new_klient_form = KlientEditForm(data=request.POST, files=request.FILES)
        
		if  new_klient_form.is_valid():
			cd = new_klient_form.cleaned_data
			nazwa = cd['nazwa']
			miejscowosc = cd['miejscowosc']
			adres = cd['adres']
			kodpocztowy = cd['kodpocztowy']
			new_klient = new_klient_form.save(commit=False)
			
			profile = get_object_or_404(Profile, user=request.user)
			new_klient.save()			
			profile.klient = new_klient
			lokacja = Lokacja.objects.create(klient=new_klient)
			lokacja.nazwa = nazwa
			lokacja.miejscowosc = miejscowosc
			lokacja.adres = adres
			lokacja.kodpocztowy = kodpocztowy
			
			profile.save()
			lokacja.save()
			klient = new_klient
			
			messages.success(request, 'Uaktualnienie profilu zakończyło się sukcesem.')
			
						
										
			return render(request, 'klient/new_firm_done.html', 						
										{'klient': klient})
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		new_klient_form = KlientEditForm()
												
	return render(request,
					'klient/new_firm.html',
						{'new_klient_form': new_klient_form})	


@login_required
def edit_firm(request, nip): 
	
	klient = get_object_or_404(Klient, nip=nip)
	lokacjas = Lokacja.objects.filter(klient=klient)
	
	if request.method == 'POST':
		klient_form = KlientEditForm(instance=klient, data=request.POST, files=request.FILES)
		if klient_form.is_valid():
			cd = klient_form.cleaned_data
			klient = klient_form.save(commit=False)
			
			klient.save()			
			
			
			messages.success(request, 'Uaktualnienie danych firmowych '\
										'zakończyło się sukcesem.')
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania danych firmowych.')
	else:
		klient_form = KlientEditForm(instance=klient)
		lokacjas = Lokacja.objects.filter(klient=klient)
												
	return render(request,
					'klient/editfirm.html',
						{'klient_form': klient_form, 'lokacjas': lokacjas})
						
						
						
@login_required
def new_lokacja(request, nip): 
	
	if request.method == 'POST':
		new_lokacja_form = LokacjaEditForm(data=request.POST, files=request.FILES)
        
		if  new_lokacja_form.is_valid():
			cd = new_lokacja_form.cleaned_data
			new_lokacja = new_lokacja_form.save(commit=False)
			
			klient = get_object_or_404(Klient, nip=nip)
			new_lokacja.klient = klient			
			new_lokacja.save()
			
						
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		new_lokacja_form = LokacjaEditForm()
												
	return render(request,
					'klient/new_lokacja.html', {'new_lokacja_form': new_lokacja_form})

					
					
@login_required
def edit_lokacja(request, nip, nazwa):
	lokacja = get_object_or_404(Lokacja, nazwa=nazwa)
	if request.method == 'POST':
		lokacja_form = LokacjaEditForm(instance=lokacja, data=request.POST, files=request.FILES)
        
		if  lokacja_form.is_valid():
			cd = lokacja_form.cleaned_data
			lokacja = lokacja_form.save(commit=False)
			
			lokacja.save()
			
						
			messages.success(request, 'Uaktualnienie profilu '\
										'zakończyło się sukcesem.')
		else:
			messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')
	else:
		lokacja_form = LokacjaEditForm(instance=lokacja)
												
	return render(request,
					'klient/editlokacja.html',
						{'lokacja_form': lokacja_form, 'lokacja': lokacja})	