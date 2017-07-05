'''
Created on 2017年6月19日

@author: Administrator
'''
import json

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.age=2  
        self.name='xiaoming'  
        
        
# myClass=MyClass()  
# #添加数据c  
# myClass.age=24  
# myClass.name='xiaoli' 
#  
# #对象转化为字典  
# myClassDict = myClass.__dict__  
# #打印字典  
# print ('dict类型==%s' % myClassDict)  
# #字典转化为json  
# myClassJson = json.dumps(myClassDict)  
# #打印json数据  
# print (myClassJson) 
#  
# newclass = json.loads(myClassJson)
# print('dict类型==%s' % newclass)
# mydemo = MyClass() 
# mydemo.__dict__ = newclass
# print(mydemo)
# print(mydemo.name+'===%d' % mydemo.age)


str = 'creditgame-sub-278081798119250283'
print(len(str))
