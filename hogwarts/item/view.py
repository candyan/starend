#-*-coding:utf-8
from django.conf import settings
from django.template import loader, Context
from django.http import HttpResponse
import urllib, urllib2, time, json

from taobaoapi import *
from hogwarts.consts import *
from sqlstore import store
every_page_size = 20

def item_update(request, num_iid):
    current_user_name = request.session['user_name'] if 'user_name' in request.session else "未登陆"
    current_item = TaobaoItem.get(num_iid)
    print current_item.auto_fill
    t = loader.get_template('templates/item_edit.html')
    c = Context({
            'tag_title': "修改物品",
            'CALLBACK_URL': CALLBACK_URL,
            'user_name': current_user_name,
            'base_url': settings.HOST_URL,
            'STATIC_URL': settings.STATIC_URL,
            'css_file': 'starend_item.css',
            'current_item': current_item,
        })
    return HttpResponse(t.render(c))

def item_delete(request, num_iid):
    top_session = request.session['top_session'] if 'top_session' in request.session else False
    t = loader.get_template('templates/finish_op.html')
    if top_session:
        sql = "delete from taobao_items where num_iid=%s"
        result = store.execute(sql, num_iid)
        if result > 0:
            item_del_method = 'taobao.item.delete'
            res_data = call_taobao_api(item_del_method, num_iid=num_iid, session=top_session)
            res_dict = read_taobao_response(res_data)
            c = Context({
                    'BACK_URL': SHOP_DETAIL_URL,
                    'finish_status': "成功"
                })
            return HttpResponse(t.render(c))
        else:
            c = Context({
                    'BACK_URL': SHOP_DETAIL_URL,
                    'finish_status': "失败"
                })
            return HttpResponse(t.render(c))
    else:
        t = loader.get_template('templates/jump_taobao_signup.html')
        c = Context({
                'CALLBACK_URL': CALLBACK_URL,
            })
        return HttpResponse(t.render(c))

def item_add(request):
    pass
