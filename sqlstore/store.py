#-*-coding:utf-8
from consts import *
import MySQLdb

def execute(sql, params):
    conn = MySQLdb.connect(
            host = DATABASE_SETTING["host"],
            user = DATABASE_SETTING["user"],
            passwd = DATABASE_SETTING["passwd"],
            db = DATABASE_SETTING["db"],
            charset = DATABASE_SETTING["charset"])
    cursor = conn.cursor()
    n = cursor.execute(sql, params)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    fs = sql.find("select")
    if fs == -1:
        return n
    else:
        return result

def executemany(sql, params):
    conn = MySQLdb.connect(
            host = DATABASE_SETTING["host"],
            user = DATABASE_SETTING["user"],
            passwd = DATABASE_SETTING["passwd"],
            db = DATABASE_SETTING["db"],
            charset = DATABASE_SETTING["charset"])
    cursor = conn.cursor()
    n = cursor.executemany(sql, params)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    fs = sql.find("select")
    if fs == -1:
        return n
    else:
        return result
