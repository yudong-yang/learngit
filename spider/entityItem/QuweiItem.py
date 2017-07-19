import urllib.request
from lxml import etree
import os


def perseUrl(url):
    send_headers = {
        'Cache-Control': 'no-cache',
        'Host': 'www.dsuu.cc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
        'Cookie': 'Hm_lvt_b0a7990a2c01e849118379472d2efba8=1500430927; Hm_lpvt_b0a7990a2c01e849118379472d2efba8=1500430932',
        'Connection': 'keep-alive'
    }

    req = urllib.request.Request(url, headers=send_headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    tree = etree.HTML(html.decode('utf-8'))
    return tree




# 获取标题
def getTitle(etree):
    titles = etree.xpath(u"//div[@class='box_wrap ajz']/article/div/div/a/@title")
    return titles

# 获取图片
def getImage(etree):
    images = etree.xpath(u"//div[@class='box_wrap ajz']/article/div/div/a/img/@data-original")
    return images


# 获取文章链接
def getLinks(etree):
    links = etree.xpath(u"//div[@class='box_wrap ajz']/article/div/div/a/@href")
    return links


# 获取发表内容
def getContents(etree):
    contents = etree.xpath(u"//div[@class='box_wrap ajz']/article/div/div[@class='exc nr']/p/text()")
    return contents


# 获取读者
def getAuthors(etree):
    authors = etree.xpath(u"//div[@class='box_wrap ajz']/article/footer/a/@title")
    return authors


# 获取发表时间
def getTimes(etree):
    times = etree.xpath(u"//div[@class='box_wrap ajz']/article/footer/span/text()")
    return times

# 获取文件扩展名，后缀名字
def file_Suffix(path):
    return os.path.splitext(path)[1]


def downLoadImg(images, page):
    x = 1
    for imgurl in images:
        loadImg(imgurl, str(page) + '-' + str(x))
        x = x + 1


def loadImg(url, x):
    try:
        # path = os.path.dirname(__file__)+'./images/'
        path ='E:/git-repo/pythonImg/quweiImg/'
        Suffix = file_Suffix(url)
        urllib.request.urlretrieve(url, path + x + Suffix)
    except Exception as err:
        print('图片下载异常' + err)
        print('异常urxl：' + url)
    finally:
        return 0;


def quwei(titles, images, links, contents, authors, times, lens):
    lists = []
    i = 0
    while i < lens:
        quwei = (titles[i], images[i], links[i], contents[i], authors[i], times[i])
        lists.append(quwei)
        i = i + 1
    return lists

#构建对象返回
def bulidlists(etree):
    titles = getTitle(etree)
    contents = getContents(etree)
    times = getTimes(etree)
    links = getLinks(etree)
    images = getImage(etree)
    authors = getAuthors(etree)
    lens = len(titles)
    lists = quwei(titles, images, links, contents, authors, times, lens)
    return lists