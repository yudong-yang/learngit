'''
Created on 2017年6月13日

@author: Administrator
'''
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from duiba import duibaSDK
from duiba import models
from duiba import duiba_class
# 数据库操作
appKey = 'EX6ngeSvZXDLW2QVdwLhVbNsSAi'
appSecret='423xTRasDF5Tv79XARiPK9ZVtj6j'

"扣积分接口"
def consume(request):
    consume_params = duibaSDK.credits_consurme(appKey, appSecret, request.GET.dict())
    ordernum=request.GET['orderNum']
    uid = consume_params['uid']
    user=models.User.objects.get(id=uid)
    usercredits=user.credits
    errorMessage=''
    status='fail'
    if len(consume_params)<=2:
        errorMessage=consume_params
        status='fail'
    else:
        status='ok'
        errorMessage='成功'
        usercredits=int(usercredits)-int(consume_params['credits'])
        models.User.objects.filter(id=uid).update(credits=usercredits)
    bizId='duiba-'+ordernum
    CreditsResult = duiba_class.consumeparam()
    CreditsResult.status=status
    CreditsResult.bizId=bizId
    CreditsResult.credits=usercredits
    CreditsResult.errorMessage=errorMessage
    msg= CreditsResult.toJosn()
    # msg = "{'status': '"+status+"','errorMessage': '"+str(errorMessage)+"','bizId': '"+bizid+"','credits': '"+str(usercredits)+"'}"
    print(msg)
    return HttpResponse(msg)


"结果通知接口"
def notify(request):
    consume_params = duibaSDK.credits_notify(appKey, appSecret, request.GET.dict())
    return HttpResponse("ok")


"结果通知接口"
def virtual(request):
    virtual_params = duibaSDK.credits_virtual(appKey, appSecret, request.GET.dict())
    ordernum=request.GET['orderNum']
    uid = virtual_params['uid']
    user=models.User.objects.get(id=uid)
    usercredits=user.credits
    errorMessage=''
    status='fail'
    if len(virtual_params)<=2:
        errorMessage=virtual_params
        status='fail'
    else:
        status='success'
        errorMessage='成功'
        usercredits=int(usercredits)+int(virtual_params['params'])
        models.User.objects.filter(id=uid).update(credits=usercredits)
    supplierBizId='virtual-'+ordernum
    VirtualResult = duiba_class.virtualparam()
    VirtualResult.status=status
    VirtualResult.supplierBizId=supplierBizId
    VirtualResult.credits=usercredits
    VirtualResult.errorMessage=errorMessage
    msg= VirtualResult.toJosn()
    print(msg)
    return HttpResponse(msg)

"免登陆和运营位置直达接口"
def autologin(request):
    if 'dbredirect' in request.GET.dict().keys():
        uid = request.GET['uid']
    else:
        uid = 'not_login'
    try:
        user = models.User.objects.get(id=uid)
        credits=user.credits
        print(credits)
    except :
         print("用户不存在") 
         uid = 'not_login'
         credits=0
    url='http://www.duiba.com.cn/autoLogin/autologin?'
    if 'dbredirect' in request.GET.dict().keys():
        redirect=request.GET['dbredirect']
        maps = duibaSDK.bulid_params(appKey,appSecret,uid,credits,redirect=''+redirect+'')
    else:
        maps = duibaSDK.bulid_params(appKey,appSecret,uid,credits) 
    auto_url = duibaSDK.build_url(url, maps)
    return HttpResponseRedirect(auto_url) 




