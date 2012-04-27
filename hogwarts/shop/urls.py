#-*-coding:utf-8
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('hogwarts.shop.view', 
        url(r'^detail/$', 'shop_detail',{'seller_cid':0, 'current_page':1}),
        url(r'^detail/(?P<seller_cid>\d+)/$', 'shop_detail',{'current_page':1}),
        url(r'^detail/(?P<seller_cid>\d+)/(?P<current_page>\d+)/$', 'shop_detail'),
)
