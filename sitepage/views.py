from django.shortcuts import render, redirect, get_object_or_404
#from .models import Product, Jh
#from django.contrib.auth.decorators import login_required
#from cart.forms import CartAddJhForm



def start(request):
		
	return render(request, 'sitepage/start.html')
