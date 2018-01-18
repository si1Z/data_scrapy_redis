#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 11:04
# @Author  : zhujinghui
# @File    : 2.py
# @Software: PyCharm
import pymysql
from datetime import datetime,timedelta

def get_last_data():
    # 'MYSQL_TABLE': 'us_reports',
    try:
        conn = pymysql.connect(host='rm-2zebj0vhwd2f6vy4w.mysql.rds.aliyuncs.com', port=3306, user='yigukeji_db', passwd='Yigukeji_dba', db='xhyg_us_stocks', charset='utf8')
        sql = "SELECT accepted_time ,cik_num FROM us_reports ORDEr by accepted_time DESC,cik_num DESC LIMIT 0,100"
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return result
    except:
        print("xxxxxxxxxxxxx")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


tmp = get_last_data()
for i in tmp:
    print(i)