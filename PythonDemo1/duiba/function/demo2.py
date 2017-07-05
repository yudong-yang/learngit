'''
Created on 2017年6月7日

@author: Administrator
'''
import traceback 
try: 
    a=123
    b=''
    c=234 
    a=b  
    b=c  
except Exception,e:  
    print Exception,":",e