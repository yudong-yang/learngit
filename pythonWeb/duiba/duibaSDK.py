'''
Created on 2017年6月8日

@author: Administrator
'''
'''
构建免登陆地址的
'''
from urllib.parse import urlencode,parse_qs
from urllib.request import urlparse
import hashlib
import time 

def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src.encode("utf-8"))
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest

def bulid_params(appKey, appSecret, uid, credits, **sets):
    params = {}
    params['appKey']=appKey
    params['appSecret']=appSecret
    params['timestamp']=int(time.time()*1000)
    params['uid']=uid
    params['credits']=credits
    for key, value in sets.items():
        params[key] = value
    return params


def sign(params):
    '对参数进行签名验证'
    sign_str=''
    keys=sorted(params.keys())
    for key in keys:
        if key!='sign':
            sign_str=sign_str + str(params[key])
    sign = get_md5_value(sign_str)
    return sign


def signVerify(appSecret,params):
    params['appSecret']=appSecret
    if params['sign']==sign(params):
        print('签名通过'+sign(params))
        return True
    else:
        return False
    

def build_url(url,params):
    '构建免登陆地址方法'
    loginUrl=url
    signstr = sign(params)
    '将签名串放入列表中'
    params['sign']=signstr
    '拼接免登陆地址时候，移除appSecret'
    del params['appSecret']
    urlparam = urlencode(params) #'对参数进行urlencode编码'
    return loginUrl+urlparam



def credits_consurme(appKey,appSecret,request_params):
    request_params['appSecret']=appSecret
    if appKey != request_params['appKey']:
        raise Exception("appKey not match !")
    elif request_params["timestamp"] =='':
        raise Exception("timestamp can't be null ! ")
    elif signVerify(appSecret,request_params)==False:
        raise Exception("sign verify fail! ")
    else:
        return request_params



def credits_virtual(appKey,appSecret,request_params):
    request_params['appSecret']=appSecret
    if appKey != request_params['appKey']:
        raise Exception("appKey not match !")
    elif request_params["timestamp"] =='':
        raise Exception("timestamp can't be null ! ")
    elif signVerify(appSecret,request_params)==False:
        raise Exception("sign verify fail! ")
    else:
        return request_params

def credits_notify(appKey,appSecret,request_params):
    request_params['appSecret']=appSecret
    if appKey != request_params['appKey']:
        raise Exception("appKey not match !")
    elif request_params["timestamp"] =='':
        raise Exception("timestamp can't be null ! ")
    elif signVerify(appSecret,request_params)==False:
        raise Exception("sign verify fail! ")
    else:
        return request_params

def qs(url):
    query = urlparse(url).query
    return dict([(k,v[0]) for k,v in parse_qs(query).items()])

appKey = '3gyWdRiPKkaMiiH6V3RUFybsdeDZ'
appSecret='4DEz67Z1VmzWVxUy5mVUnZoS2d8v'
uid='17035'
credits=100
trs = 'redirect'
maps = bulid_params(appKey,appSecret,uid,credits,transfer=''+trs+'')



auto_url = build_url('http://www.duiba.com.cn/autoLogin/autologin?',maps)
#print("免登陆地址如下：")
#print(auto_url)
#strurl='/duiba/notify/normal?uid=15652&success=true&errorMessage=&bizId=dbmarket-34959550477665C0250&sign=96d73c1455415c336e32b9e96fa7ba36&orderNum=34959550477665C0250&appKey=3gyWdRiPKkaMiiH6V3RUFybsdeDZ&timestamp=1496825828194&'
#params=qs(strurl)
#msg = credits_notify(appKey,appSecret,params)
# print(msg)
