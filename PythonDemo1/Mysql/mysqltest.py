'''
Created on 2017年7月4日

@author: Administrator
'''
import os
import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test',charset="utf8")
# 创建游标
cursor = conn.cursor()
  
# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from users ")

  
row_1 = cursor.fetchone()

print(row_1)
row_2 = cursor.fetchmany(3)
for row in row_2:
    print(row[0])

conn.commit()
  
# 关闭游标
cursor.close()
# 关闭连接
conn.close()