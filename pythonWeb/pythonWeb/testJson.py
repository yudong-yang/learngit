'''
Created on 2017年6月19日

@author: Administrator
'''
from duiba import duiba_class


param = duiba_class.consumeparam()
param.status='success'
param.bizId=12323
param.credits=234
param.errorMessage='玉东'
msg = param.toJosn()
print(msg)