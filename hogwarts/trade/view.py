#-*-coding:utf-8
from django.conf import settings
from django.template import loader, Context
from django.http import HttpResponse
import urllib, urllib2, time, json

from taobaoapi import *
from hogwarts.consts import *

every_page_size = 20

def trade_center(request, current_page):
    print current_page
    current_page = int(current_page)
    current_user_name = request.session['user_name'] if 'user_name' in request.session else "未登陆"
    trade_list = TaobaoTrade.get_by_username(current_user_name)
    current_trade_list = trade_list[(current_page - 1) * every_page_size:current_page * every_page_size]
    page_count = len(trade_list) / every_page_size + 1
    t = loader.get_template('templates/trade_detail.html')
    c = Context({
            'tag_title': "订单",
            'CALLBACK_URL': CALLBACK_URL,
            'user_name': current_user_name,
            'base_url': settings.HOST_URL,
            'STATIC_URL': settings.STATIC_URL,
            'css_file': 'starend_trade.css',
            'current_trade_list': current_trade_list,
            'page_count': page_count,
            'page_list': range(1, page_count + 1),
            'trade_base_url': TRADE_URL,
            'current_page': current_page,
            'next_page': current_page + 1,
            'prev_page': current_page - 1,
        })
    return HttpResponse(t.render(c))

def trade_detail(request, tid):
    return HttpResponse(1)
