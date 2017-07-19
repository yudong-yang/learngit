'''
Created on 2017年7月4日

@author: Administrator
'''

import pymysql
from pachong.firstdemo import neihanduanzi
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test',charset="utf8")
# 创建游标
cursor = conn.cursor()


url='http://neihanshequ.com/'

etree = neihanduanzi.perseUrl(url)
titles = neihanduanzi.getTitle(etree)
contents = neihanduanzi.getContent(etree)
links = neihanduanzi.getLink(etree)
len = len(titles)
lists = neihanduanzi.bulidNeihan(titles, links, contents, len)
# 执行SQL，并返回收影响行数
for i in range(len):
    try:
        effect_row = cursor.execute("insert into contents(title,url,content)values(%s,%s,%s)",lists[i] )
        print(effect_row)
        # 提交数据
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()



  
