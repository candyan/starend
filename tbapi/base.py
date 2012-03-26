#-*-coding:utf-8
from taobaoapi import *
import hashlib, time, urllib, urllib2, json

def taobao_sign(params, secret):
    keys = params.keys()
    keys.sort()
    hashchars = secret + ''.join([x + params[x] for x in keys]) + secret

    return hashlib.md5(hashchars).hexdigest().upper()

class TaobaoAPI:
    def __init__(self):
        self.params = {
        'app_key': APP_KEY,
        'format': 'json',
        'method': '',
        'sign_method': 'md5',
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
        'v': '2.0',
    }

    def setFields(self, fields):
        self.params['fields'] = fields

    def setNick(self, nick):
        self.params['nick'] = nick

    def setFormat(self, tbformat):
        self.params['format'] = tbformat

    def setMethod(self, method):
        self.params['method'] = method

    def setSession(self, session):
        self.params['session'] = session

    def sendRequest(self, secret):
        self.params['sign'] = taobao_sign(self.params, APP_SECRET)
        args_url = urllib.urlencode(self.params)
        url = API_URL + '?' + args_url
        url_open = urllib2.urlopen(url).read()
        return url_open
