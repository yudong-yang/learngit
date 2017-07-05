'''
Created on 2017年7月4日

@author: Administrator
'''

import os
import pymysql
import time  
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test',charset="utf8")
# 创建游标
cursor = conn.cursor()
values = []
for i in range(10000):
    user = ('xiaoming','123434','Man','xiaomingdemo')
    values.append(user)
# 执行SQL，并返回收影响行数
now=time.strftime("%M:%S") 
try:
    effect_row = cursor.executemany("insert into users(userName,passWord,user_sex,nick_name)values(%s,%s,%s,%s)", values)
    print(effect_row)
    #提交数据
    conn.commit()
except Exception as err:  
    print(err)  
finally:  
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
end=time.strftime("%M:%S") 
print(now,':',end)

  
