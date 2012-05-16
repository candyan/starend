#-*-coding:utf-8
from sqlstore import store
from consts import *
class TaobaoUser:
    def __init__(self, user_id, user_name, city, state, seller_credit_level, seller_credit_score, seller_credit_total, seller_credit_good):
        self.user_id = user_id
        self.user_name = user_name
        self.city = city
        self.state = state
        self.seller_credit_level = seller_credit_level
        self.seller_credit_score = seller_credit_score
        self.seller_credit_total = seller_credit_total
        self.seller_credit_good = seller_credit_good

    @classmethod
    def get(cls, user_id):
        r = store.execute("select * from taobao_user where user_id=%s", user_id)
        if r:
            return TaobaoUser(*r[0])
        return False

    @classmethod
    def gets(cls, user_ids):
        return [cls.get(user_id) for user_id in user_ids]

    @classmethod
    def get_by_name(cls, user_name):
        r = store.execute("select * from taobao_user where user_name=%s", user_name)
        if r:
            return TaobaoUser(*r[0])
        return False

class TaobaoShop:
    def __init__(self, sid, cid, user_name, title, shop_desc, bulletin, pic_path, shop_score_item, shop_score_service, shop_score_delivery):
        self.sid = sid
        self.cid = cid
        self.user_name = user_name
        self.title = title
        self.desc = shop_desc
        self.bulletin = bulletin
        self.pic_path = LOGO_BASE_URL + pic_path
        self.score_item = shop_score_item
        self.score_service = shop_score_service
        self.score_delivery = shop_score_delivery
        self.shop_url = 'http://shop' + str(self.sid) + '.taobao.com'
    
    @classmethod
    def get(cls, user_name):
        r = store.execute("select * from taobao_shop where user_name=%s", user_name)
        if r:
            return TaobaoShop(*r[0])
        return False

class TaobaoItem:
    def __init__(self, num_iid, detail_url, title, user_name, item_type, item_desc, auction_point, property_alias, cid, seller_cid, pic_url, item_num, valid_thru, list_time, delist_time, stuff_status, price, post_fee, express_fee, ems_fee, has_discount, freight_payer, approve_status, auto_fill):
        self.num_iid = num_iid
        self.detail_url = detail_url
        self.title = title
        self.user_name = user_name
        self.desc = item_desc
        self.item_type = "一口价" if item_type == 'fixed' else "拍卖"
        self.auction_point = auction_point
        self.property_alias = property_alias
        self.cid = cid
        self.seller_cid = seller_cid.split(',')
        self.seller_cid.remove('')
        if self.seller_cid:
            self.seller_cid.remove('')
        self.pic_url = pic_url if pic_url else DEFAULT_PIC_URL
        self.num = item_num
        self.list_time = list_time
        self.delist_time = delist_time
        self.stuff_status = stuff_status
        self.price = price
        self.post_fee = post_fee
        self.express_fee = express_fee
        self.ems_fee = ems_fee
        self.has_discount = has_discount
        self.freight_payer = freight_payer
        self.approve_status = "出售中" if approve_status == "onsale" else "库存中" if approve_status == "instock" else "已下架" 
        self.auto_fill = auto_fill
    
    @classmethod
    def get(cls, num_iid):
        r = store.execute("select * from taobao_items where num_iid=%s", num_iid)
        if r:
            return TaobaoItem(*r[0])
        return False
    
    @classmethod
    def gets(cls, num_iids):
        return [cls.get(num_iid) for num_iid in num_iids]

    @classmethod
    def gets_by_username(cls, user_name):
        r = store.execute("select num_iid from taobao_items where user_name=%s", user_name)
        if r:
            num_iids = []
            for item in r:
                num_iids.append(item[0])
            return cls.gets(num_iids)
        return []

    @staticmethod
    def filter_items_by_seller_cid(item_list, seller_cid):
        if seller_cid == 0:
            return item_list
        filtered_item_list = []
        for item in item_list:
            if seller_cid in item.seller_cid:
                filtered_item_list.append(item)
        return filtered_item_list

class TaobaoSellerCat:
    def __init__(self, cid, parent_cid, name, sort_order, cat_type, pic_url):
        self.cid = cid
        self.parent_cid = parent_cid
        self.cat_name = name
        self.sort_order = sort_order
        self.cat_type = cat_type
        self.pic_url = pic_url
        self.childs = []

    @classmethod
    def get(cls, cid):
        r = store.execute("select cid,parent_cid,name,sort_order,cat_type,pic_url from taobao_seller_cat where cid=%s", cid)
        if r:
            return TaobaoSellerCat(*r[0])
        return False

    @classmethod
    def gets(cls, cids):
        return [cls.get(cid) for cid in cids]

    @classmethod
    def gets_by_username(cls, user_name):
        r = store.execute("select cid from taobao_seller_cat where user_name=%s", user_name)
        if r:
            cids = []
            for item in r:
                cids.append(item[0])
            return cls.gets(cids)
        return []

    @staticmethod
    def create_seller_cat_tree(seller_cat_list):
        if not seller_cat_list:
            return []
        seller_cat_list.sort(key=lambda x:x.parent_cid)
        parent_count = 0
        for seller_cat in seller_cat_list:
            if seller_cat.parent_cid != 0:
                break;
            else:
                parent_count += 1
        root = seller_cat_list[0:parent_count]
        childs = seller_cat_list[parent_count:]
        root_dict = {}
        for cat in root:
            root_dict[cat.cid] = cat
        for child in childs:
            root_dict[child.parent_cid].childs.append(child)
        for cat in root_dict:
            if root_dict[cat].childs:
                root_dict[cat].childs.sort(key=lambda x:x.sort_order)
        return root_dict

class TaobaoTrade:
    def __init__(self, tid, num, num_iid, status, title, buyer_name, trade_type, price, point_fee, create_time, pay_time, end_time, payment, consign_time, buyer_message, post_fee):
        self.tid = tid
        self.num = num
        self.item = TaobaoItem.get(num_iid)
        self.status = TRADE_STATUS[status]
        self.title = title
        self.buyer_name = buyer_name
        self.trade_type = trade_type
        self.price = price
        self.point_fee = point_fee
        self.create_time = create_time
        self.pay_time = pay_time
        self.end_time = end_time
        self.payment = payment
        self.consign_time = consign_time
        self.buyer_message = buyer_message
        self.post_fee = post_fee

    @classmethod
    def get(cls, tid):
        r = store.execute("select tid,num,num_iid,status,title,buyer_name,trade_type,price,point_fee,create_time,pay_time,end_time,payment,consign_time,buyer_message,post_fee from taobao_trades where tid=%s", tid)
        if r:
            return TaobaoTrade(*r[0])
        return False

    @classmethod
    def gets(cls, tids):
        return [cls.get(tid) for tid in tids]

    @classmethod
    def get_by_username(cls, user_name):
        r = store.execute("select tid from taobao_trades where user_name=%s", user_name)
        if r:
            tids = []
            for item in r:
                tids.append(item[0])
            return cls.gets(tids)
        return []
