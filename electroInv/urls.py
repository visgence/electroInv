from django.conf.urls import include, url
import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^digikey/$', views.digikey, name='digikey'),
    url(r'^digikey/import/$', views.importDigikey, name='import-digikey'),

    url(r'^octopart/$', views.octopart, name='octopart'),
    url(r'^octopart/update/$', views.octopartUpdate, name='octopart-update'),

    url(r'^part/$', views.part, name='part'),
    url(r'^vendor/$', views.vendor, name="vendor"),
    url(r'^type/$', views.type, name="type"),
    url(r'^manufacture/$', views.manufacture, name='manufacture'),
    url(r'^package/$', views.package, name='package'),
    url(r'^log/$', views.log, name="log"),
    url(r'^login-page/$', views.login_page, name='login-page')
]
