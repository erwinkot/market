from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^product/$', views.prod_list, name='jh_list'),
	url(r'^product/(?P<producent_slug>[-\w]+)/$', views.prod_list_producent, name='jh_list_by_producent'),
	#url(r'^product/(?P<producent_slug>[-\w]+)/$', views.prod_list_producent, name='jh_list_by_producent'),
	url(r'^stomatologia/$', views.prod_list_stomat, name='prod_list_stomat'),
	url(r'^product/(?P<producent_slug>[-\w]+)/stomatologia/$', views.prod_list_stomat_producent, name='prod_list_stomat_by_producent'),
	url(r'^sip/$', views.prod_list_sip, name='prod_list_sip'),
	url(r'^product/(?P<producent_slug>[-\w]+)/sip/$', views.prod_list_sip_producent, name='prod_list_sip_by_producent'),
	url(r'^ds/$', views.prod_list_ds, name='prod_list_ds'),
	url(r'^product/(?P<producent_slug>[-\w]+)/ds/$', views.prod_list_ds_producent, name='prod_list_ds_by_producent'),
	url(r'^sc/$', views.prod_list_sc, name='prod_list_sc'),
	url(r'^product/(?P<producent_slug>[-\w]+)/sc/$', views.prod_list_sc_producent, name='prod_list_sc_by_producent'),
	url(r'^jed/$', views.prod_list_jed, name='prod_list_jed'),
	url(r'^product/(?P<producent_slug>[-\w]+)/jed/$', views.prod_list_jed_producent, name='prod_list_jed_by_producent'),
	url(r'^biuro/$', views.prod_list_biuro, name='prod_list_biuro'),
	url(r'^product/(?P<producent_slug>[-\w]+)/biuro/$', views.prod_list_biuro_producent, name='prod_list_biuro_by_producent'),
	url(r'^(?P<product_slug>[-\w]+)/$', views.prod_detail, name='jh_list_by_product'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
		views.jh_detail,
		name='jh_detail'),
]
