#!/usr/bin/python3
# -*- codeing = utf-8 -*-
# @Time : 2021/8/30 22:13
# @Author: 王治国
# @File : test.py
# @Software:PyCharm
import sqlite3

datalist = []
con = sqlite3.connect("movie.db")
cur = con.cursor()
sql = "select * from movie250"
data = cur.execute(sql)
print(data)
for item in data:
    print(item)
    datalist.append(item)
# print(datalist)
cur.close()
con.close()