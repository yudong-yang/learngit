'''
Created on 2017年6月30日

@author: Administrator
模仿网上案例，模拟爬虫，写一个网络爬虫工具，完全抄写
'''

import lxml
import urllib.request
url='file:///D:/JAVA/PythonDemo1/duiba/http/test1.html'



def perseUrl(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def content(html):
    # 内容分割的标签
    str2 = '<div class="content">'
    content = str(html , encoding = "utf-8").partition(str2)[2]
    str1 = '<div class="pagination">'
    content = content.partition(str1)[0]
    return content


def title(content,beg = 0):
    # 思路是利用str.index()和序列的切片
    try:
        title_list = []
        while True:   
            num1 = content.index('"_blank">',beg)
            num2 = content.index('</a>',num1)
            title_list.append(content[num1+9:num2])
            beg = num2
        
    except ValueError:
        return title_list
     
     
def description(content,beg = 0):
    # 思路是利用str.index()和序列的切片
    try:
        title_list = []
        while True:   
            num1 = content.index('"note">',beg)
            num2 = content.index('</p>',num1)
            title_list.append(content[num1+7:num2])
            beg = num2
        
    except ValueError:
        return title_list    


def imgaes(content,beg = 0):
    # 思路是利用str.index()和序列的切片
    try:
        title_list = []
        while True:   
            num1 = content.index('src',beg)
            num2 = content.index('/>',num1)
            title_list.append(content[num1+4:num2])
            beg = num2
        
    except ValueError:
        return title_list


htmlstr = perseUrl(url)
text= content(htmlstr)
listtitle =title(text,0) 
listdescription =description(text,0) 
for i in listdescription.__len__():
    print(listdescription[i])
    