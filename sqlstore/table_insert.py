#-*-coding:utf-8
from consts import *
from sqlstore import store
import MySQLdb

def taobao_shop_insert(store_list):
    conn = MySQLdb.connect(
            host = DATABASE_SETTING["host"],
            user = DATABASE_SETTING["user"],
            passwd = DATABASE_SETTING["passwd"],
            db = DATABASE_SETTING["db"],
            charset = DATABASE_SETTING["charset"])
    cursor = conn.cursor()
    sql_delete = "delete from taobao_shop where sid=%s"
    cursor.execute(sql_delete, store_list[0])
    conn.commit()
    sql_insert = "insert into taobao_shop value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    n = cursor.execute(sql_insert, store_list)
    conn.commit()
    cursor.close()
    conn.close()
    if n == 1:
        return True
    else:
        return False

def taobao_user_insert(store_list):
    conn = MySQLdb.connect(
            host = DATABASE_SETTING["host"],
            user = DATABASE_SETTING["user"],
            passwd = DATABASE_SETTING["passwd"],
            db = DATABASE_SETTING["db"],
            charset = DATABASE_SETTING["charset"])
    cursor = conn.cursor()
    sql_delete = "delete from taobao_user where user_id=%s"
    cursor.execute(sql_delete, store_list[0])
    conn.commit()
    sql_insert = "insert into taobao_user value(%s,%s,%s,%s,%s,%s,%s,%s)"
    n = cursor.execute(sql_insert, store_list)
    conn.commit()
    cursor.close()
    conn.close()
    if n == 1:
        return True
    else:
        return False

def taobao_items_insert(store_list):
    conn = MySQLdb.connect(
            host = DATABASE_SETTING["host"],
            user = DATABASE_SETTING["user"],
            passwd = DATABASE_SETTING["passwd"],
            db = DATABASE_SETTING["db"],
            charset = DATABASE_SETTING["charset"])
    cursor = conn.cursor()
    sql_delete = "delete from taobao_items where user_name=%s"
    cursor.execute(sql_delete, store_list[0][3])
    conn.commit()
    sql_insert = "insert into taobao_items value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    n = cursor.executemany(sql_insert, store_list)
    conn.commit()
    cursor.close()
    conn.close()
    if n == len(store_list):
        return True
    else:
        return False

def taobao_auth_itemcats_insert(store_list):
    conn = MySQLdb.connect(
            host = DATABASE_SETTING["host"],
            user = DATABASE_SETTING["user"],
            passwd = DATABASE_SETTING["passwd"],
            db = DATABASE_SETTING["db"],
            charset = DATABASE_SETTING["charset"])
    cursor = conn.cursor()
    sql_delete = "delete from taobao_auth_itemcats where user_name=%s"
    cursor.execute(sql_delete, store_list[0][6])
    conn.commit()
    sql_insert = "insert into taobao_auth_itemcats value(%s,%s,%s,%s,%s,%s,%s)"
    n = cursor.executemany(sql_insert, store_list)
    conn.commit()
    cursor.close()
    conn.close()
    if n == len(store_list):
        return True
    else:
        return False

def taobao_auth_brands_insert(store_list):
    conn = MySQLdb.connect(
            host = DATABASE_SETTING["host"],
            user = DATABASE_SETTING["user"],
            passwd = DATABASE_SETTING["passwd"],
            db = DATABASE_SETTING["db"],
            charset = DATABASE_SETTING["charset"])
    cursor = conn.cursor()
    sql_delete = "delete from taobao_auth_brands where user_name=%s"
    cursor.execute(sql_delete, store_list[0][4])
    conn.commit()
    sql_insert = "insert into taobao_auth_brands value(%s,%s,%s,%s,%s)"
    n = cursor.executemany(sql_insert, store_list)
    conn.commit()
    cursor.close()
    conn.close()
    if n == len(store_list):
        return True
    else:
        return False

def taobao_seller_cat_insert(store_list):
    sql_del = "delete from taobao_seller_cat where user_name=%s"
    user_name = store_list[0][-1]
    res_del = store.execute(sql_del, user_name)
    sql_insert = "insert into taobao_seller_cat value(%s, %s, %s, %s, %s, %s, %s)"
    res_insert = store.executemany(sql_insert, store_list)
    if res_insert == len(store_list):
        return True
    else:
        return False

def taobao_trades_insert(store_list):
    sql_del = "delete from taobao_trades where user_name=%s"
    user_name = store_list[0][-1]
    res_del = store.execute(sql_del, user_name)
    sql_insert = "insert into taobao_trades value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    res_insert = store.executemany(sql_insert, store_list)
    if res_insert == len(store_list):
        return True
    else:
        return False
