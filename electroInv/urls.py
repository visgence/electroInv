from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'electroInv.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^login-page/$', 'login_page', name='login-page'),
    )
