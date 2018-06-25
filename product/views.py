from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Jh, Producent, Cotojest
from .forms import FiltrCotojestForm
from django.contrib.auth.decorators import login_required
#from cart.forms import CartAddJhForm



def prod_list(request, product_slug=None):
	product = None
	
	if request.method == 'POST':
	
		filtrcotojest_form = FiltrCotojestForm(request.POST)
		products = Product.objects.all()
		producents = Producent.objects.all()
		jhs = Jh.objects.filter(available=True)
		
		if filtrcotojest_form.is_valid():
			cd = filtrcotojest_form.cleaned_data
			products = products.filter(cotojest=cd['cotojest'])
			
			
	
			return render(request, 'product/product/list.html', {'product': product, 
																	'products': products, 
																	'producents': producents,
																	'filtrcotojest_form': filtrcotojest_form})
	else:
		products = Product.objects.all()
		producents = Producent.objects.all()
		jhs = Jh.objects.filter(available=True)
		filtrcotojest_form = FiltrCotojestForm()
		
		return render(request, 'product/product/list.html', {'product': product, 
																	'products': products, 
																	'producents': producents,
																	'filtrcotojest_form': filtrcotojest_form})
		
		
	
def prod_list_producent(request, producent_slug):
	product = None
	if producent_slug:
		producents = Producent.objects.all()
		producent = get_object_or_404(Producent, slug=producent_slug)
		products = Product.objects.filter(producent=producent)
		if request.method == 'POST':
		
			filtrcotojest_form = FiltrCotojestForm(request.POST)
			if filtrcotojest_form.is_valid():
				cd = filtrcotojest_form.cleaned_data
				products = products.filter(cotojest=cd['cotojest'])
				
	
				return render(request, 'product/product/list.html', {'product': product, 
																		'products': products, 
																		'producent': producent,
																		'producents': producents,
																		'filtrcotojest_form': filtrcotojest_form})
															
															
		else:
			filtrcotojest_form = FiltrCotojestForm()
			producents = Producent.objects.all()
			producent = get_object_or_404(Producent, slug=producent_slug)
			products = Product.objects.filter(producent=producent)
			
		
			return render(request, 'product/product/list.html', {'product': product, 
																	'products': products, 
																	'producent': producent,
																	'producents': producents,
																	'filtrcotojest_form': filtrcotojest_form})														


																	
																	
def prod_list_stomat(request):
	product = None
	products = Product.objects.filter(profilmat=1)
	producents = Producent.objects.all()
	jhs = Jh.objects.filter(available=True)
	if request.method == 'POST':
		filtrcotojest_form = FiltrCotojestForm(request.POST)
		if filtrcotojest_form.is_valid():
			cd = filtrcotojest_form.cleaned_data
			products = products.filter(cotojest=cd['cotojest'])
		
	
			return render(request, 'product/product/listprofil1.html', {'product': product, 
																			'products': products, 
																			'producents': producents,
																			'filtrcotojest_form': filtrcotojest_form})
	else:
		products = Product.objects.filter(profilmat=1)
		producents = Producent.objects.all()
		jhs = Jh.objects.filter(available=True)
		filtrcotojest_form = FiltrCotojestForm()
		
		return render(request, 'product/product/listprofil1.html', {'product': product, 
																	'products': products, 
																	'producents': producents,
																	'filtrcotojest_form': filtrcotojest_form})																
				



				

def prod_list_stomat_producent(request, producent_slug):
	product = None
	products = Product.objects.filter(profilmat=1)
	producents = Producent.objects.all()
	if producent_slug:
		producent = get_object_or_404(Producent, slug=producent_slug)
		products = products.filter(producent=producent)
		jhs = Jh.objects.filter(available=True)
		
		if request.method == 'POST':
			filtrcotojest_form = FiltrCotojestForm(request.POST)
			if filtrcotojest_form.is_valid():
				cd = filtrcotojest_form.cleaned_data
				products = products.filter(cotojest=cd['cotojest'])
				
	
				return render(request, 'product/product/listprofil1.html', {'product': product, 
																				'products': products, 
																				'producent': producent,
																				'producents': producents,
																				'filtrcotojest_form': filtrcotojest_form})
																		
		else:
			filtrcotojest_form = FiltrCotojestForm()
			
			
		
			return render(request, 'product/product/listprofil1.html', {'product': product, 
																			'products': products, 
																			'producent': producent,
																			'producents': producents,
																			'filtrcotojest_form': filtrcotojest_form})																
	
	


def prod_list_sip(request):
	product = None
	products = Product.objects.filter(profilmat=2)
	producents = Producent.objects.all()
	#jhs = Jh.objects.filter(available=True)
	
	return render(request, 'product/product/listprofil2.html', {'product': product, 'products': products, 'producents': producents})
	
	
def prod_list_sip_producent(request, producent_slug=None):
	product = None
	products = Product.objects.filter(profilmat=2)
	producents = Producent.objects.all()
	if producent_slug:
		producent = get_object_or_404(Producent, slug=producent_slug)
		products = products.filter(producent=producent)
		
		jhs = Jh.objects.filter(available=True)
	
	return render(request, 'product/product/listprofil2.html', {'product': product, 
																	'products': products, 
																	'producents': producents})


def prod_list_jed(request):
	product = None
	products = Product.objects.filter(profilmat=3)
	producents = Producent.objects.all()
	#jhs = Jh.objects.filter(available=True)
	
	return render(request, 'product/product/listprofil3.html', {'product': product, 'products': products, 'producents': producents})
	
	
def prod_list_jed_producent(request, producent_slug=None):
	product = None
	products = Product.objects.filter(profilmat=3)
	producents = Producent.objects.all()
	if producent_slug:
		producent = get_object_or_404(Producent, slug=producent_slug)
		products = products.filter(producent=producent)
		
		jhs = Jh.objects.filter(available=True)
	
	return render(request, 'product/product/listprofil3.html', {'product': product, 
																	'products': products, 
																	'producents': producents})
	
	
def prod_list_ds(request):
	product = None
	products = Product.objects.filter(profilmat=4)
	producents = Producent.objects.all()
	#jhs = Jh.objects.filter(available=True)
	
	return render(request, 'product/product/listprofil4.html', {'product': product, 'products': products, 'producents': producents})
	
	
def prod_list_ds_producent(request, producent_slug=None):
	product = None
	products = Product.objects.filter(profilmat=4)
	producents = Producent.objects.all()
	if producent_slug:
		producent = get_object_or_404(Producent, slug=producent_slug)
		products = products.filter(producent=producent)
		
		jhs = Jh.objects.filter(available=True)
	
	return render(request, 'product/product/listprofil4.html', {'product': product, 
																	'products': products, 
																	'producents': producents})
	
	
	
def prod_list_sc(request):
	product = None
	products = Product.objects.filter(profilmat=5)
	producents = Producent.objects.all()
	#jhs = Jh.objects.filter(available=True)
	
	return render(request, 'product/product/listprofil5.html', {'product': product, 
																	'products': products,
																	'producents': producents})
	
	
def prod_list_sc_producent(request, producent_slug=None):
	product = None
	products = Product.objects.filter(profilmat=5)
	producents = Producent.objects.all()
	if producent_slug:
		producent = get_object_or_404(Producent, slug=producent_slug)
		products = products.filter(producent=producent)
		
		jhs = Jh.objects.filter(available=True)
	
	return render(request, 'product/product/listprofil5.html', {'product': product, 
																	'products': products, 
																	'producents': producents})
	
	
	
def prod_list_biuro(request):
	product = None
	products = Product.objects.filter(profilmat=6)
	producents = Producent.objects.all()
	#jhs = Jh.objects.filter(available=True)
	
	return render(request, 'product/product/listprofil6.html', {'product': product, 
																	'products': products,
																	'producents': producents})
	
	
def prod_list_biuro_producent(request, producent_slug=None):
	product = None
	products = Product.objects.filter(profilmat=6)
	producents = Producent.objects.all()
	if producent_slug:
		producent = get_object_or_404(Producent, slug=producent_slug)
		products = products.filter(producent=producent)
		
		jhs = Jh.objects.filter(available=True)
	
	return render(request, 'product/product/listprofil6.html', {'product': product, 
																	'products': products, 
																	'producents': producents})
	

def prod_detail(request, product_slug):
	
	if product_slug:
		product = get_object_or_404(Product, slug=product_slug)
		jhs = Jh.objects.filter(available=True,jh=product)
	#cart_jh_form = CartAddProductForm()
	
	return render(request, 'product/product/list_prod.html', {'product': product, 'jhs': jhs, })


def jh_detail(request, id, slug):
	jh = get_object_or_404(Jh, id=id, slug=slug, available=True)
	#cart_jh_form = CartAddJhForm()
	
	return render(request, 'product/product/detail.html', {'jh': jh})

