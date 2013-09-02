from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'electroInv.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^digikey/$', 'digikey', name='digikey'),
    url(r'^part/$', 'part'),
    url(r'^vendor/$', 'vendor'),
    url(r'^type/$', 'type'),
    url(r'^manufacture/$', 'manufacture'),
    url(r'^package/$', 'package'),
    url(r'^log/$', 'log'),
    url(r'^login-page/$', 'login_page', name='login-page'),
    )
