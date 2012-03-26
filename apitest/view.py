#-*-coding:utf-8
from django.http import HttpResponse
from taobaoapi import *
import urllib, urllib2, time, json

def getuser(request):
    params = {
        'app_key': APP_KEY,
        'fields': 'user_id',
        'format': 'json',
        'method': 'taobao.user.get',
        'nick': 'liuyanhp',
        'sign_method': 'md5',
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
        'v': '2.0',
    }

    params['sign'] = taobao_sign(params, APP_SECRET)
    args = urllib.urlencode(params)

    url = "http://gw.api.tbsandbox.com/router/rest?" + args
    url_open = urllib2.urlopen(url).read()
    return HttpResponse(url_open)
