#-*-coding:utf-8
from django.template import loader, Context
from django.http import HttpResponse
from taobaoapi import *
import urllib, urllib2, time, json

def syncdb(request):
    t = loader.get_template('templates/test_list.html')
    c = Context({
        "test_list": SYNC_DB_LIST,
    })
    return HttpResponse(t.render(c))

def syncTaobaoUser(request):

    return HttpResponse("hello")
