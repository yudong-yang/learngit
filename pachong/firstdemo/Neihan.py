'''
Created on 2017年7月4日

@author: Administrator
'''
import os
import pymysql
from firstdemo import neihanduanzi
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test', charset="utf8")
# 创建游标
cursor = conn.cursor()


# 执行SQL，并返回收影响行数
effect_row = cursor.executemany("insert into city(title,url,content)values(%s,%s,%s)", [("1234","上海","东方明珠在上海"),('1234',"广州","广州小蛮腰")])


conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()