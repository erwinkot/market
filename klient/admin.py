from django.contrib import admin
from .models import Catkli, Klient, Lokacja, Detale, Grupa


class CatkliAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'slug']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Catkli, CatkliAdmin)


class KlientAdmin(admin.ModelAdmin):
	list_display = ['id', 'nazwa', 'slug']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Klient, KlientAdmin)


class LokacjaAdmin(admin.ModelAdmin):
	list_display = ['klient', 'nazwa', 'slug']
	
admin.site.register(Lokacja, LokacjaAdmin)


class DetaleAdmin(admin.ModelAdmin):
	list_display = ['klient', 'rabatz', 'rabatr', 'kredytlimit', 'peyment']
	
admin.site.register(Detale, DetaleAdmin)


class GrupaAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'slug']
	
admin.site.register(Grupa, GrupaAdmin)