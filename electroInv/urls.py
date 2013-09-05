from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'electroInv.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
   
    url(r'^digikey/$', 'digikey', name='digikey'),
    url(r'^digikey/import/$', 'importDigikey', name='import-digikey'),
    
    url(r'^octopart/$', 'octopart', name='octopart'),
    url(r'^octopart/update/$', 'octopartUpdate', name='octopart-update'),

    url(r'^part/$', 'part', name='part'),
    url(r'^vendor/$', 'vendor', name="vendor"),
    url(r'^type/$', 'type', name="type"),
    url(r'^manufacture/$', 'manufacture', name='manufacture'),
    url(r'^package/$', 'package', name='package'),
    url(r'^log/$', 'log', name="log"),
    url(r'^login-page/$', 'login_page', name='login-page'),
)
