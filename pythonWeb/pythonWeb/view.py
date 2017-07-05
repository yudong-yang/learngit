'''
Created on 2017年6月9日

@author: Administrator
'''
from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
#     return HttpResponse("Hello world ! ")