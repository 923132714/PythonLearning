#!/usr/bin/env python
#coding=utf-8

import pymysql

#创建数据库连接，注意这里我加入了charset和cursorclass参数
conn = pymysql.connect(
    host = "lunareclipse.net.cn",
    user = "python",
    password = "lalala427",
    database = "python",
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor)
#获取游标
cursor = conn.cursor()
cursor.execute("SELECT * FROM Test;")
#fetchall：获取所有的数据，默认以元祖的方式返回，如果你指定了cursorclass = pymysql.cursors.DictCursor，则以dict的方式返回
#result = cursor.fetchall()
#for row in result:
#    print("id是%d,name是%s，age是%d"%(row["id"],row["name"],row["age"]))
#fetchone：获取剩余数据的第一条数据
result = cursor.fetchone()
print(result)
#fetchmany:获取剩余数据的前2条数据
#result = cursor.fetchmany(2)
#print(result)
cursor.close()
conn.close()