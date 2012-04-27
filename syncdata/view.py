#-*-coding:utf-8
from django.template import loader, Context
from django.http import HttpResponse
from django.conf import settings
from taobaoapi import *
from hogwarts.consts import *
from syncdata import *
import json

def syncdb(request):
    session = request.GET['top_session'] if "top_session" in request.GET.keys() else ""
    if session != "":
        result_user = sync_user_data(session)
        if result_user in ERROR_LIST.values():
            return HttpResponse(result_user)
        result_shop = sync_shop_data(result_user[1])
        result_items = sync_items_data(session, result_user[1])
        result_auth = sync_auth_data(session, result_user[1])
        result_seller_cat = sync_seller_cat(result_user[1])
        request.session['user_name'] = result_user[1]
        request.session['top_session'] = session
        result = result_user and result_shop and result_items and result_auth and result_seller_cat
        if result:
            t = loader.get_template('templates/sync_data.html')
            c = Context({
                    'INDEX_URL': SHOP_DETAIL_URL,
                })
            return HttpResponse(t.render(c))
        else:
            return HttpResponse("同步失败")
    else:
        return HttpResponse("You have not log in.")
    return HttpResponse(t.render(c))
