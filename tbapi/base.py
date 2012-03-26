#-*-coding:utf-8
from taobaoapi import *
import hashlib, time

def taobao_sign(params, secret):
    keys = params.keys()
    keys.sort()
    hashchars = secret + ''.join([x + params[x] for x in keys]) + secret

    return hashlib.md5(hashchars).hexdigest().upper()

class TaobaoAPI:
    def __init__(self):
        params = {
            'app_key': APP_KEY,
            'format': 'json',
            'method': '',
            'sign_method': 'md5',
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'v': '2.0',
        }

    def setFields(self, fields):
        params['fields'] = fields

    def setNick(self, nick):
        params['nick'] = nick

    def setFormat(self, tbformat):
        params['format'] = tbformat
