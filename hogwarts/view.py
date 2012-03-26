#-*-coding:utf-8
from django.template import loader, Context
from django.http import HttpResponse
from taobaoapi import *
import urllib, urllib2, hashlib, time, json

def index(requset):
    t = loader.get_template('templates/index.html')
    c = Context()
    return HttpResponse(t.render(c))

def api(request):
    t = loader.get_template('templates/api_list.html')
    c = Context({
        "api_list": API_LIST,
    })
    return HttpResponse(t.render(c))
