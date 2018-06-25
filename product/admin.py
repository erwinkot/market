from django.contrib import admin
from .models import Producent, Profilmat, Product, Jh, Cotojest


class ProducentAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'slug', 'firma', 'kraj', 'miasto']
	list_filter = ['kraj', 'miasto']
	prepopulated_fields = {'slug': ('nazwa',)}
	
admin.site.register(Producent, ProducentAdmin)



class ProfilmatAdmin(admin.ModelAdmin):
	list_display = ['id', 'nazwa', 'slug']
	prepopulated_fields = {'slug': ('nazwa',)}
	
admin.site.register(Profilmat, ProfilmatAdmin)


class CotojestAdmin(admin.ModelAdmin):
	list_display = ['id', 'nazwa', 'slug']
	prepopulated_fields = {'slug': ('nazwa',)}
	
admin.site.register(Cotojest, CotojestAdmin)



class JhInline(admin.TabularInline):
	model = Jh
	raw_id_fields = ['jh']
	prepopulated_fields = {'slug': ('name',)}
	
	
	
class ProductAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'slug', 'producent', 'cotojest', 'profilmat']
	list_filter = ['producent', 'cotojest', 'profilmat']
	prepopulated_fields = {'slug': ('nazwa',)}
	inlines = [JhInline]
	
admin.site.register(Product, ProductAdmin)



