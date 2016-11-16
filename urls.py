from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/electroInv/')),
    url(r'^electroInv/', include('electroInv.urls')),
    url(r'^chucho/', include('chucho.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += staticfiles_urlpatterns()
