#-*-encoding:utf-8
from taobaoapi import *
from sqlstore.table_insert import *
import json

def sync_user_data(session):
    user_method = 'taobao.user.get'
    user_fields = 'user_id,nick,location,seller_credit'
    dict_data = call_taobao_api(user_method, fields=user_fields, session=session)
    #dict_data = read_taobao_response(res_data)
    if dict_data in ERROR_LIST.keys():
        return ERROR_LIST[dict_data]
    sqlstore_list = [
            dict_data['user_id'],
            dict_data['nick'],
            dict_data['location']['city'] if 'city' in dict_data['location'].keys() else "",
            dict_data['location']['state'] if 'state' in dict_data['location'].keys() else "",
            dict_data['seller_credit']['level'],
            dict_data['seller_credit']['score'],
            dict_data['seller_credit']['total_num'],
            dict_data['seller_credit']['good_num'],
    ]
    result = taobao_user_insert(sqlstore_list)
    return result, sqlstore_list[1]

def sync_shop_data(nick):
    shop_method = 'taobao.shop.get'
    shop_fields = 'sid,cid,title,nick,desc,bulletin,pic_path,shop_score'
    dict_data = call_taobao_api(shop_method, fields=shop_fields, nick=nick)
    #dict_data = read_taobao_response(res_data)
    sqlstore_list = [
        dict_data["sid"],
        dict_data["cid"],
        dict_data["nick"],
        dict_data["title"],
        dict_data["desc"],
        dict_data["bulletin"],
        dict_data["pic_path"],
        dict_data["shop_score"]["item_score"],
        dict_data["shop_score"]["service_score"],
        dict_data["shop_score"]["delivery_score"],
    ]
    result = taobao_shop_insert(sqlstore_list)
    return result

def get_items_list(session, nick):
    page_size = '100'
    get_items_method = 'taobao.items.get'
    get_items_fields = 'num_iid'
    item_list = call_taobao_api(get_items_method, fields=get_items_fields, nicks=nick, page_size=page_size)
    #item_list = read_taobao_response(res_dict)
    items_len = len(item_list)
    group_count = items_len / 20
    current_num = 0
    item_group = []
    while current_num != group_count:
        item_group.append(item_list[current_num * 20:(current_num + 1) * 20])
        current_num += 1
    item_group.append(item_list[(group_count - 1) * 20:])
    return item_group

def sync_items_data(session, nick):
    items_list_method = 'taobao.items.list.get'
    items_list_fields = 'num_iid,detail_url,title,nick,type,desc,auction_point,property_alias,cid,seller_cids,pic_url,num,valid_thru,list_time,delist_time,stuff_status,price,post_fee,express_fee,ems_fee,has_discount,freight_payer,approve_status,auto_fill'
    item_group = get_items_list(session, nick)
    if len(item_group[0]) > 0:
        for item_list in item_group:
            num_iids = ""
            for item in item_list:
                num_iids = num_iids + str(item['num_iid']) + ','
            items_list_data = call_taobao_api(items_list_method, fields=items_list_fields, session=session, num_iids=num_iids)
            #items_list_data = read_taobao_response(res_data)
            sql_lists = []
            for item_list in items_list_data:
                sqlstore_list = [
                        item_list['num_iid'],
                        item_list['detail_url'],
                        item_list['title'],
                        item_list['nick'],
                        item_list['type'],
                        item_list['desc'],
                        item_list['auction_point'],
                        item_list['property_alias'],
                        item_list['cid'],
                        item_list['seller_cids'],
                        item_list['pic_url'] if 'pic_url' in item_list.keys() else "",
                        item_list['num'],
                        item_list['valid_thru'],
                        item_list['list_time'],
                        item_list['delist_time'],
                        item_list['stuff_status'],
                        item_list['price'],
                        item_list['post_fee'],
                        item_list['express_fee'],
                        item_list['ems_fee'],
                        item_list['has_discount'],
                        item_list['freight_payer'],
                        item_list['approve_status'],
                        item_list['auto_fill'] if 'auto_fill' in item_list.keys() else "",
                ]
                sql_lists.append(sqlstore_list)
            result = taobao_items_insert(sql_lists)
        return result
    return 1

def sync_auth_data(session, user_name):
    itemcats_method = 'taobao.itemcats.authorize.get'
    itemcats_fields = 'brand.vid,brand.name,brand.pid,brand.prop_name,item_cat.cid,item_cat.name,item_cat.status,item_cat.sort_order,item_cat.parent_cid,item_cat.is_parent'
    data_list = call_taobao_api(itemcats_method, fields=itemcats_fields, session=session)
    #data_list = read_taobao_response(res_data)
    item_cat_list = data_list['item_cats']['item_cat'] if 'item_cat' in data_list['item_cats'].keys() else []
    item_brand_list = data_list['brands']['brand'] if 'brand' in data_list['brands'].keys() else []
    cat_sqlstore = []
    brand_sqlstore = []
    result_cats = False
    result_brands = False
    if len(item_cat_list) > 0:
        for item_cat in item_cat_list:
            sqlstore = [
                    item_cat['cid'],
                    item_cat['parent_cid'],
                    item_cat['name'],
                    item_cat['is_parent'],
                    item_cat['status'],
                    item_cat['sort_order'],
                    user_name,
            ]
            cat_sqlstore.append(sqlstore)
        result_cats = taobao_auth_itemcats_insert(cat_sqlstore)
    if len(item_brand_list) > 0:
        for item_brand in item_brand_list:
            sqlstore = [
                    item_brand['vid'],
                    item_brand['name'],
                    item_brand['pid'],
                    item_brand['prop_name'],
                    user_name,
            ]
            brand_sqlstore.append(sqlstore)
        result_brands = taobao_auth_brands_insert(brand_sqlstore)
    return result_cats, result_brands

def sync_seller_cat(nick):
    method_name = 'taobao.sellercats.list.get'
    seller_cat_list = call_taobao_api(method_name, nick=nick)
    #seller_cat_list = read_taobao_response(res_data)
    if seller_cat_list:
        seller_cat_sqlstore = []
        for seller_cat in seller_cat_list:
            sqlstore = [
                    seller_cat['cid'],
                    seller_cat['parent_cid'],
                    seller_cat['name'],
                    seller_cat['sort_order'],
                    seller_cat['type'],
                    seller_cat['pic_url'],
                    nick,
            ]
            seller_cat_sqlstore.append(sqlstore)
        res_insert_cat = taobao_seller_cat_insert(seller_cat_sqlstore)
        return res_insert_cat
    else:
        return -1

def sync_trades(session, nick):
    store_list = []
    has_next = True
    method_name = 'taobao.trades.sold.get'
    page_size = '100'
    page_no = 1
    fields = 'tid,num,num_iid,status,type,price,title,point_fee,created,pay_time,end_time,buyer_nick,payment,seller_nick,consign_time,buyer_message,post_fee,seller_alipay_no,receiver_name,receiver_state,receiver_city,receiver_district,receiver_address,receiver_zip,seller_alipay_no,seller_mobile,seller_name,seller_email,shipping_type'
    while(has_next):
        trade_list = call_taobao_api(method_name, fields=fields, session=session, page_size=page_size, page_no=str(page_no))
        #trade_list = read_taobao_response(res_data)
        for trade in trade_list[0]:
            sqlstore = [
                    trade['tid'],
                    trade['num'],
                    trade['num_iid'],
                    trade['status'],
                    trade['title'],
                    trade['buyer_nick'],
                    trade['type'],
                    trade['price'],
                    trade['point_fee'],
                    trade['created'],
                    trade['pay_time'] if 'pay_time' in trade.keys() else '0000-00-00 00:00:00',
                    trade['end_time'] if 'end_time' in trade.keys() else '0000-00-00 00:00:00',
                    trade['payment'],
                    trade['consign_time'] if 'consign_tiem' in trade.keys() else '0000-00-00 00:00:00',
                    trade['buyer_message'] if 'buyer_message' in trade.keys() else "",
                    trade['post_fee'],
                    trade['seller_alipay_no'],
                    trade['seller_name'],
                    trade['seller_mobile'],
                    trade['seller_email'],
                    trade['receiver_name'],
                    trade['receiver_state'],
                    trade['receiver_city'],
                    trade['receiver_district'],
                    trade['receiver_address'],
                    trade['receiver_zip'],
                    trade['shipping_type'],
                    nick,
            ]
            store_list.append(sqlstore)
            has_next = trade_list[1]
            page_no = page_no + 1
    res_insert_trades = taobao_trades_insert(store_list)
    return res_insert_trades
