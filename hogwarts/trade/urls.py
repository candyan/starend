#-*-coding:utf-8
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('hogwarts.trade.view', 
        url(r'^detail/$', 'trade_center', {'current_page':1}),
        url(r'^detail/(?P<current_page>\d+)/$', 'trade_center'),
        url(r'^(?P<tid>\d+)/$', 'trade_detail'),
)
