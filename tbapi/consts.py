#-*-coding:utf-8
from django.conf import settings
SAND_BOX = settings.DEBUG
APP_KEY = "12612953"
APP_SECRET = "sandbox60c4dbe9709850b953e8a9519" if SAND_BOX else "de8924360c4dbe9709850b953e8a9519"
API_URL = "http://gw.api.tbsandbox.com/router/rest" if SAND_BOX else "http://gw.api.taobao.com/router/rest"
DEFAULT_PIC_URL = "http://mini.tbsandbox.com/minisandbox/assets/img/nopicture.gif" if SAND_BOX else "http://"
LOGO_BASE_URL = "http://logo.taobao.com/shop-logo"
CALLBACK_URL = "http://container.api.tbsandbox.com/container?appkey=%s&encode=utf-8" % APP_KEY if SAND_BOX else "http://container.api.taobao.com/container?appkey=%s&encode=utf-8" % APP_KEY
ERROR_LIST = {
    'call_taobao_api_error': "no session and nick",
    'Invalid session:Session expired': "session过期了",
    'Invalid signature': "无效的签名",
}
TRADE_STATUS = {
        'TRADE_NO_CREATE_PAY': "没有创建支付宝交易",
        'WAIT_SELLER_SEND_GOODS': "等待卖家发货",
        'WAIT_BUYER_PAY': "等待买家付款",
        'WAIT_BUYER_CONFIRM_GOODS': "等待买家确认收货",
        'TRADE_BUYER_SIGNED': "买家已签收",
        'TRADE_FINISHED': "交易成功",
        'TRADE_CLOSED': "付款以后用户退款成功，交易自动关闭",
        'TRADE_CLOSED_BY_TAOBAO': "付款以前，卖家或买家主动关闭交易",
    }
