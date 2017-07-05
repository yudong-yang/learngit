'''
Created on 2017年6月13日

@author: Administrator
'''
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators import csrf

from duiba import models
 
# 数据库操作
def testdb(request):
    if 'id' in request.GET:
        id = request.GET['id']
        print(id)
        test1 = models.Test(name='runoob', ages=27)
        test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
        print(request.GET['q'])
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
