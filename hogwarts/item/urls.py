#-*-coding:utf-8
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('hogwarts.item.view', 
        url(r'^add/$', 'item_add'),
        url(r'^update/(?P<num_iid>\d+)/$', 'item_update'),
        url(r'^del/(?P<num_iid>\d+)/$', 'item_delete'),
)
