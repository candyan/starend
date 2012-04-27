#-*-coding:utf-8
SAND_BOX = True
APP_KEY = "12525857"
APP_SECRET = "sandbox76af6a8ba6cc535a3addba62f" if SAND_BOX else "7a5937cb302b60a5cfa78406d58a4fd9"
API_URL = "http://gw.api.tbsandbox.com/router/rest" if SAND_BOX else "http://gw.api.taobao.com/router/rest"
DEFAULT_PIC_URL = "http://mini.tbsandbox.com/minisandbox/assets/img/nopicture.gif" if SAND_BOX else "http://"
LOGO_BASE_URL = "http://logo.taobao.com/shop-logo"
CALLBACK_URL = "http://container.api.tbsandbox.com/container?appkey=%s&encode=utf-8" % APP_KEY if SAND_BOX else "http://container.api.taobao.com/container?appkey=%s&encode=utf-8" % APP_KEY
ERROR_LIST = {
    'call_taobao_api_error': "no session and nick",
    'Invalid session:Session expired': "session过期了",
}
