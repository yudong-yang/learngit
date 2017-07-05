'''
Created on 2017年7月4日

@author: Administrator
'''
import dbm

db = dbm.open('websites','w')
db['www.apache.org']='apache home page'
db['www.mysql.org']='mysql home page'
db['www.google.org']='google home page'

if db['www.apache.org']!=None:
    print('Found www.apache.org')
else:
    print('Error: Missing Item ! ')
del db['www.google.org']
    
for key in db.keys():
    print('key==',key,'value==',db[key])
db.close()