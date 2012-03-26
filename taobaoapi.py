#-*-coding:utf-8
from django.conf import settings

if settings.TAOBAOAPI_PATH:
    import sys
    sys.path.insert(0, settings.TAOBAOAPI_PATH)

from consts import *
from base import TaobaoAPI
