#-*-coding:utf-8
from django.conf import settings

if settings.TAOBAOAPI_PATH:
    import sys
    if not settings.TAOBAOAPI_PATH in sys.path:
        sys.path.insert(0, settings.TAOBAOAPI_PATH)

from consts import *
from base import TaobaoAPI, call_taobao_api
from model import TaobaoUser, TaobaoShop, TaobaoItem, TaobaoSellerCat, TaobaoTrade
