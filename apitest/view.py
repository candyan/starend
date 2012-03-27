#-*-coding:utf-8
from django.template import loader, Context
from django.http import HttpResponse
from taobaoapi import *
import urllib, urllib2, time, json

def api(request):
    t = loader.get_template('templates/test_list.html')
    c = Context({
        "test_list": API_TEST_LIST,
    })
    return HttpResponse(t.render(c))

def getuser(request):
    test_api = TaobaoAPI()
    test_api.setMethod('taobao.user.get')
    test_api.setNick('liuyanhp')
    test_api.setFields('user_id,nick,seller_credit')
    data = test_api.sendRequest(APP_SECRET)
    #data = json.loads(data)
    #data = data["user_get_response"]["user"]
    return HttpResponse(data)

def getshopinfo(request):
    test_api = TaobaoAPI()
    test_api.setMethod('taobao.shop.get')
    test_api.setNick('liuyan_test')
    test_api.setFields('sid,cid,title,nick,desc,bulletin,pic_path,created,modified')
    data = test_api.sendRequest(APP_SECRET)
    return HttpResponse(data)
