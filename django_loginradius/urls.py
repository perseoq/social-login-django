from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^connect/$', 'django_loginradius.views.connect', name='lr_connect'),
)
