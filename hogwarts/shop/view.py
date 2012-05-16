#-*-coding:utf-8
from django.conf import settings
from django.template import loader, Context
from django.http import HttpResponse
import urllib, urllib2, time, json

from taobaoapi import *
from hogwarts.consts import *

every_page_size = 20

def shop_detail(request, seller_cid, current_page):
    current_page = int(current_page)
    user_name = request.session['user_name'] if 'user_name' in request.session.keys() else False 
    current_user = TaobaoUser.get_by_name(user_name) if user_name else False
    if not current_user:
        t = loader.get_template('templates/jump_taobao_signup.html')
        c = Context({
                'tag_title': "淘宝登陆",
                'CALLBACK_URL': CALLBACK_URL,
            })
        return HttpResponse(t.render(c))
    else:
        current_shop = TaobaoShop.get(current_user.user_name)
        current_items_list = TaobaoItem.gets_by_username(current_user.user_name)
        filter_item_list = TaobaoItem.filter_items_by_seller_cid(current_items_list, seller_cid)
        current_seller_cat_list = TaobaoSellerCat.gets_by_username(current_user.user_name)
        current_seller_cat_tree = TaobaoSellerCat.create_seller_cat_tree(current_seller_cat_list)
        page_list = range(1, len(filter_item_list) / every_page_size + 2)
        shop_info_list = [
                    ['店铺名称', current_shop.title],
                    ['所在地区', current_user.state + " " + current_user.city],
                    ['卖家信用', current_user.seller_credit_score],
                    ['商品描述评分', current_shop.score_item],
                    ['服务态度评分', current_shop.score_service],
                    ['发货速度评分', current_shop.score_delivery],
                ]
        t = loader.get_template('templates/shop_detail.html')
        c = Context({
            'tag_title': "店铺详情",
            'CALLBACK_URL': CALLBACK_URL,
            'user_name':current_user.user_name,
            'base_url': settings.HOST_URL,
            'STATIC_URL': settings.STATIC_URL,
            'css_file': 'starend_shop_detail.css',
            'shop_info_list': shop_info_list,
            'shop_url': current_shop.shop_url,
            'bullet': current_shop.bulletin,
            'shop_desc': current_shop.desc,
            'shop_item_list': filter_item_list[(current_page - 1) * every_page_size:(current_page * every_page_size)],
            'page_list': page_list,
            'page_count': len(page_list),
            'current_page': current_page,
            'prev_page': current_page - 1,
            'next_page': current_page + 1,
            'shop_detail_url': SHOP_DETAIL_URL,
            'seller_cid': seller_cid,
            'item_url': ITEM_URL,
            'seller_cat_tree': current_seller_cat_tree,
        })
        return HttpResponse(t.render(c))
