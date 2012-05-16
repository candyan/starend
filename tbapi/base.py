#-*-coding:utf-8
from consts import *
import hashlib, time, urllib, urllib2, json


def call_taobao_api(method, fields=False, session=False, num_iid=False, nick=False, page_size=False, num_iids=False, nicks=False, page_no=False):
    taobao_api = TaobaoAPI()
    if session:
        taobao_api.setSession(session)
    if nick:
        taobao_api.setNick(nick)
    if nicks:
        taobao_api.setNicks(nicks)
    if num_iid:
        taobao_api.setNum_iid(num_iid)
    if num_iids:
        taobao_api.setNum_iids(num_iids)
    if fields:
        taobao_api.setFields(fields)
    if page_size:
        taobao_api.setPageSize(page_size)
    if page_no:
        taobao_api.setPageNo(page_no)
    taobao_api.setMethod(method)
    return taobao_api.sendRequest()

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

    def setPageNo(self, page_no):
        self.params['page_no'] = page_no

    def setPageSize(self, page_size):
        self.params['page_size'] = page_size

    def setNum_iids(self, num_iids):
        self.params['num_iids'] = num_iids

    def setNicks(self, nicks):
        self.params['nicks'] = nicks
    
    def setNum_iid(self, num_iid):
        self.params['num_iid'] = num_iid

    def taobao_sign(self):
        keys = self.params.keys()
        keys.sort()
        hashchars = APP_SECRET + ''.join([x + self.params[x] for x in keys]) + APP_SECRET
        return hashlib.md5(hashchars).hexdigest().upper()

    def read_taobao_response(self, res_dict):
        if 'user_get_response' in res_dict.keys():
            return res_dict['user_get_response']['user']
        elif 'shop_get_response' in res_dict.keys():
            return res_dict['shop_get_response']['shop']
        elif 'items_get_response' in res_dict.keys():
            count = res_dict['items_get_response']['total_results']
            return res_dict['items_get_response']['items']['item'] if count > 0 else []
        elif 'items_onsale_get_response' in res_dict.keys():
            count = res_dict['items_onsale_get_response']['total_results']
            return res_dict['items_onsale_get_response']['items']['item'] if count > 0 else []
        elif 'items_inventory_get_response' in res_dict.keys():
            count = res_dict['items_inventory_get_response']['total_results']
            return res_dict['items_inventory_get_response']['items']['item'] if count > 0 else []
        elif 'items_list_get_response' in res_dict.keys():
            return res_dict['items_list_get_response']['items']['item']
        elif 'itemcats_authorize_get_response' in res_dict.keys():
            return res_dict['itemcats_authorize_get_response']['seller_authorize']
        elif 'sellercats_list_get_response' in res_dict.keys():
            if 'seller_cats' in res_dict['sellercats_list_get_response'].keys():
                return res_dict['sellercats_list_get_response']['seller_cats']['seller_cat']
            else:
                return []
        elif 'trades_sold_get_response' in res_dict.keys():
            count = res_dict['trades_sold_get_response']['total_results']
            has_next = True if 'has_next' in res_dict['trades_sold_get_response'] else False
            return res_dict['trades_sold_get_response']['trades']['trade'], has_next if count > 0 else [], has_next
        elif 'error_response' in res_dict.keys():
            return res_dict['error_response']['msg']
        else:
            return ""

    def sendRequest(self):
        self.params['sign'] = self.taobao_sign()
        args_url = urllib.urlencode(self.params)
        url = API_URL + '?' + args_url
        url_open = urllib2.urlopen(url).read()
        response_data = json.loads(url_open)
        return self.read_taobao_response(response_data)
