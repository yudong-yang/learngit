

import pymysql
from spider.Dao.dbconfig import dbconfig

def insertdemo(sql , lists):
    dbc = dbconfig()
    conn = pymysql.connect(host=dbc.host, port=dbc.port, user=dbc.user, passwd=dbc.passwd, db=dbc.db, charset=dbc.charset) # 创建游标
    cursor = conn.cursor()
    # 执行SQL，并返回收影响行数
    try:
        effect_row = cursor.executemany(sql , lists) #提交数据
        conn.commit()
    except Exception as err:
        conn.rollback()
        print(err)
    finally:
        cursor.close()
    # 关闭连接
        conn.close()
        # 关闭游标
        return effect_row

def delete(sql):
    dbc = dbconfig()
    db = pymysql.connect(host=dbc.host, port=dbc.port, user=dbc.user, passwd=dbc.passwd, db=dbc.db, charset=dbc.charset)  # 创建游标
    cursor = db.cursor()
    try:
        effect_row = cursor.execute(sql)
        print(effect_row)
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    finally:
        cursor.close()
        db.close()

def select(sql):
    # 打开数据库连接
    dbc = dbconfig()
    conn = pymysql.connect(host=dbc.host, port=dbc.port, user=dbc.user, passwd=dbc.passwd, db=dbc.db,
                       charset=dbc.charset)  # 创建游标
    cursor = conn.cursor()

    # SQL 查询语句
    try:
        # 执行SQL语句
        cursor.execute(sql)
         # 获取所有记录列表
        results = cursor.fetchall()
        titles=[]
        for row in results:
            titles.append(row[1])

        return titles
    except:
        # 发生错误时回滚
        conn.rollback()
    finally:
        cursor.close()
        conn.close()