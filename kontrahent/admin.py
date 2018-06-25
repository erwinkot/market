from django.contrib import admin
from .models import Wojewodztwo, Powiat, Gmina, Miejscowosc

class WojewodztwoAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'slug', 'wojewoda']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Wojewodztwo, WojewodztwoAdmin)


class PowiatAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'slug', 'starosta', 'wojewodztwo']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Powiat, PowiatAdmin)



class GminaAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'slug', 'wojt', 'powiat']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Gmina, GminaAdmin)



class MiejscowoscAdmin(admin.ModelAdmin):
	list_display = ['id', 'nazwa', 'slug', 'profil', 'gmina']
	prepopulated_fields = {'slug': ('nazwa',)}

admin.site.register(Miejscowosc, MiejscowoscAdmin)
