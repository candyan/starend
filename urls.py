from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index/$', 'hogwarts.view.index'),
    url(r'^api/$', 'hogwarts.view.api'),
    url(r'^api/getuser/$', 'apitest.view.getuser'),
    url(r'^api/getshopinfo/$', 'apitest.view.getshopinfo'),
    # Examples:
    # url(r'^$', 'starend.views.home', name='home'),
    # url(r'^starend/', include('starend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', include(admin.site.urls)),
)
