from django.conf.urls import include, url
import views
import apiviews
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/vendor', apiviews.VendorViewSet)
router.register(r'api/type', apiviews.TypeViewSet)
router.register(r'api/manufacture', apiviews.ManufactureViewSet)

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
    url(r'^login-page/$', views.login_page, name='login-page'),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
