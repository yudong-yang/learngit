import time
from spider.entityItem import QuweiItem as quwei
from spider.Dao import DBControl as DB

#过滤已存在的项目
def sublist(lists1 , lists2):
    sublist = []
    for b in lists1:
        if b[0] in lists2:
            sublist.append(b)
    for i in sublist:
        lists1.remove(i)
    return lists1

def deleteBytitles(titles):
    listtitle=[]
    for title in titles:
        listtitle .append(title)
    listtitle = listtitle
    titlesstr = str(listtitle)[1:-1]
    sql = "DELETE FROM quwei where titles in (%s) " % titlesstr
    DB.delete(sql)

def findByTitles(titles):
    listitle = []
    for title in titles:
        listitle.append(title)
    titlestr = str(listitle)[1:-1]
    sql = "SELECT * FROM quwei  WHERE titles in (%s)" % titlestr
    return DB.select(sql)

def batchsave(lists):
    titles=[]
    for list in lists:
        titles.append(list[0])
    subtitles = findByTitles(titles)
    sublists = sublist(lists , subtitles)
    sql ="insert into quwei(titles, images, links, contents, authors, times)values(%s,%s,%s,%s,%s,%s)"
    print(sql)
    num = DB.insertdemo(sql,lists)
    return num
now=time.strftime("%M:%S")
for page in range(3,10):
    url = 'http://www.dsuu.cc/quwei-category/joke/page/%d' % page + '/'
    etree = quwei.perseUrl(url)
    lists = quwei.bulidlists(etree)
    num = batchsave(lists)
    print('插入条数',num)
end=time.strftime("%M:%S")
print(now,':',end)