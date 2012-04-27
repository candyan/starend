from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^shop/', include('hogwarts.shop.urls')),
    url(r'^item/', include('hogwarts.item.urls')),
    url(r'^syncdb/', include('syncdata.urls')),
    # Examples:
    # url(r'^$', 'starend.views.home', name='home'),
    # url(r'^starend/', include('starend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
