from django.conf.urls import url
from . import views

urlpatterns = [
	
    #url(r'^$', views.realestate_start, name='startre'),
	#url(r'^cennik/$', views.cennik, name='cennik'),
	#url(r'^regulamin/$', views.regulamin, name='regulamin'),
	#url(r'^edfi/$', views.edit_firm, name='editfirm'),
	#url(r'^pitka/$', views.probino, name='probino'),
	url(r'^fspr/$', views.firma_sprawdzana, name='sprfirma'),
	url(r'^fspr/(?P<nip>[0-9]+)/$', views.edit_firm, name='editfirm'),
	url(r'^nip/(?P<nip>[0-9]+)/$', views.edit_firm, name='editfirm'),
	url(r'^nip/(?P<nip>[0-9]+)/lokacja/$', views.new_lokacja, name='new_lokacja'),
	#url(r'^account/edit/(?P<nip>[0-9]+)/$', views.edit_firm, name='editfirm'),
	url(r'^newfi/$', views.new_firm, name='new_firm'),
	#url(r'^newfi/$', views.new_firm_done, name='new_firm_done'),
	url(r'^nip/$', views.potw_nip, name='potw_nip'),
	url(r'^nip/(?P<nip>[0-9]+)/(?P<nazwa>[-\w]+)/$', views.edit_lokacja, name='editlokacja'),
		
]