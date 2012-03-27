from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('syncdata.view',
    url(r'^$', 'syncdb'),
    url(r'^tbuser/$', 'syncTaobaoUser'),
)
