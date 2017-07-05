'''
Created on 2017年6月30日

@author: Administrator
模仿网上案例，模拟爬虫，写一个网络爬虫工具，完全抄写
'''

'''
博海拾贝爬虫试验
'''

import codecs
from lxml import etree
import urllib.request


url='https://bohaishibei.com/post/category/main/page/2/'

def perseUrl(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    tree = etree.HTML(html.lower().decode('utf-8'))
    return tree

#获取标题
def getTitle(etree):
    titles = etree.xpath(u"//div[@class='content']/article/header/h2/a")
    return titles

#获取发表时间
def getTimes(etree):
    times = etree.xpath(u"//div[@class='content']/article/p[@class='text-muted time']")
    return times

#获取发表内容
def getNote(etree):
    notes = etree.xpath(u"//div[@class='content']/article/p[@class='note']")
    return notes

#获取图片
def getImage(etree):
    images = etree.xpath(u"//div[@class='content']/article/p[@class='focus']/a/img/@src")
    return images


def suburl(tag1,tag2,url):
    num1 = url.index(tag1)
    num2 = url.index(tag2)
    start = num1+len(tag1)
    end=num2+len(tag2)
    suburl = url[start:end]
    return suburl

def downLoadImg(images):
    x = 0
    for imgurl in images:
        subimg = suburl('src=','.jpg',imgurl)
        print()
        urllib.request.urlretrieve(subimg,'D:/JAVA/pachong/firstdemo/image/%s.jpg' % x)
        x+=1
        


tree = perseUrl(url)
gettitles = getImage(tree)   
#down = downLoadImg(gettitles)
for title in gettitles:
    subimg = suburl('src=','.jpg',title)
    print(subimg)




