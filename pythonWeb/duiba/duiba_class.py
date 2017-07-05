'''
Created on 2017年6月19日

@author: Administrator
'''
import json

class consumeparam(object):
    '''
    classdocs 兑吧响应json
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.status='true'
        self.errorMessage=''
        self.bizId=''
        self.credits=0
        
    def toJosn(self):
        '''
        object  to JOSN
        '''
        myClassDict = self.__dict__
        myClassJson = json.dumps(myClassDict,ensure_ascii=False)  #json.dumps在默认情况下，对于非ascii字符生成的是相对应的字符编码，而非原始字符
        return myClassJson
    
class virtualparam(object):
    '''
    classdocs 兑吧响应json
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.status=''
        self.errorMessage=''
        self.supplierBizId=''
        self.credits=0
        
    def toJosn(self):
        '''
        object  to JOSN
        '''
        myClassDict = self.__dict__
        myClassJson = json.dumps(myClassDict,ensure_ascii=False)  #json.dumps在默认情况下，对于非ascii字符生成的是相对应的字符编码，而非原始字符
        return myClassJson
    

