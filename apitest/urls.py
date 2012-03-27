#-*-coding:utf-8
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apitest.view',
    url(r'^$', 'api'),
    url(r'^getuser', 'getuser'),
    url(r'^getshopinfo', 'getshopinfo'),
)
