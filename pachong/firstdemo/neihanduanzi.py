'''
Created on 2017年7月4日
内涵段子
@author: Administrator
'''
import codecs
from lxml import etree
import urllib.request

class Neihan():
    def __init__(self, title, url, content):
        self.title = title
        self.url = url
        self.content = content

url='http://neihanshequ.com/'

def perseUrl(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    tree = etree.HTML(html.lower().decode('utf-8'))
    return tree



#获取标题
def getContent(etree):
    titles = etree.xpath(u"//div[@class='content']/ul/li//div[@class='content-wrapper']//p")
    return titles


#获取url
def getLink(etree):
    urllinks = etree.xpath(u"//div[@class='content']/ul/li//div[@class='content-wrapper']/a/@href")
    return urllinks

#获取内容
def getTitle(etree):
    titles = etree.xpath(u"//div[@class='content']/ul/li//span[@class='name']")
    return titles

def bulidNeihan(titles,links,contents,len):
    lists = []
    i=0
    while i< len:
        niehan = (titles[i].text,links[i],contents[i].text)
        lists.append(niehan)
        i=i+1
    return lists





