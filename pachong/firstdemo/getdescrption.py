'''
Created on 2017年7月4日

@author: Administrator
'''
import urllib.request
import re
def getHtml(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def getImg(html):
    reg = r'src=".+?\.png"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,str(html))
    x = 0
    for imgurl in imglist:
        print(imgurl)
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1



html = getHtml("https://tieba.baidu.com/p/5199234125")

print(getImg(html))