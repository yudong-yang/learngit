import urllib.request
from lxml import etree
import os


def perseUrl(url):
    send_headers = {
        'Cache-Control': 'no-cache',
        'Host': 'bohaishibei.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
        'Cookie': '_pk_ref.2.159a=%5B%22%22%2C%22%22%2C1499337730%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DNGCPEimJM6GlCm_UemF2Gt1YbYMfQIjSQpj8SRWwC4TOzx8XONLyvuMS3NKyT_ak%26wd%3D%26eqid%3Da19abb210003a2dc00000005595e13ef%22%5D; _pk_id.2.159a=c899ca6c17b6293f.1498801768.8.1499339407.1499337730.; _pk_ses.2.159a=*; Hm_lvt_202cd84cd7fad9d4f42420d54bacd365=1499085931,1499149704,1499337730,1499339180; Hm_lpvt_202cd84cd7fad9d4f42420d54bacd365=1499339407',
        'Connection': 'keep-alive'
    }

    req = urllib.request.Request(url, headers=send_headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    tree = etree.HTML(html.decode('utf-8'))
    return tree




# 获取标题
def getTitle(etree):
    titles = etree.xpath(u"//div[@class='content']/article/header/h2/a")
    return titles


# 获取发表时间
def getTimes(etree):
    times = etree.xpath(u"//div[@class='content']/article/p[@class='text-muted time']")
    return times


# 获取文章链接
def getLinks(etree):
    links = etree.xpath(u"//div[@class='content']//header/h2/a/@href")
    return links


# 获取发表内容
def getContents(etree):
    contents = etree.xpath(u"//div[@class='content']/article/p[@class='note']")
    return contents


# 获取图片
def getImage(etree):
    images = etree.xpath(u"//div[@class='content']/article/p[@class='focus']/a/img/@src")
    return images


# 获取阅读数量
def getViews(etree):
    views = etree.xpath(u"//div[@class='content']//span[@class='post-views']")
    return views


# 获取文件扩展名，后缀名字
def file_Suffix(path):
    return os.path.splitext(path)[1]


def suburl(tag1, tag2, url):
    num1 = url.index(tag1)
    num2 = url.index(tag2)
    start = num1 + len(tag1)
    end = num2
    suburl = url[start:end]
    return suburl


def downLoadImg(images, page):
    x = 1
    for imgurl in images:
        url = suburl('src=', '&', imgurl)
        loadImg(url, str(page) + '-' + str(x))
        x = x + 1


def loadImg(url, x):
    try:
        # path = os.path.dirname(__file__)+'./images/'
        path ='E:/git-repo/pythonImg/bohaiImg/'
        Suffix = file_Suffix(url)
        urllib.request.urlretrieve(url, path + x + Suffix)
    except Exception as err:
        print('图片下载异常' + err)
        print('异常urxl：' + url)
    finally:
        return 0;


def bohsb(titles, images, links, contents, views, times, lens):
    lists = []
    i = 0
    while i < lens:
        #        content = highpoints.sub(u'', contents[i].text)
        bhsb = (
        titles[i].text, suburl('src=', '&', images[i]), links[i], contents[i].text, views[i].text, times[i].text)
        lists.append(bhsb)
        i = i + 1
    return lists


def bulidlists(etree):
    titles =getTitle(etree)
    contents = getContents(etree)
    times = getTimes(etree)
    links = getLinks(etree)
    images = getImage(etree)
    views = getViews(etree)
    lens = len(titles)
    lists = bohsb(titles, images, links, contents, views, times, lens)
    return lists
