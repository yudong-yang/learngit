import time
from spider.entityItem import bohaiItem as bhsb
from spider.Dao import DBControl as DB

#去掉重复元素
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
    sql = "DELETE FROM bohaisb where titles in (%s) " % titlesstr
    print(sql)
    DB.delete(sql)

def findByTitles(titles):
    listitle = []
    for title in titles:
        listitle.append(title)
    titlestr = str(listitle)[1:-1]
    sql = "SELECT * FROM bohaisb  WHERE titles in (%s)" % titlestr
    return DB.select(sql)

def batchsave(lists):
    titles=[]
    for list in lists:
        titles.append(list[0])
    subtitles = findByTitles(titles)
    sublists = sublist(lists , subtitles)
    sql ="insert into bohaisb(titles, images, links, contents, views, times)values(%s,%s,%s,%s,%s,%s)"
    num = DB.insertdemo(sql,sublists)
    return num
now=time.strftime("%M:%S")
for page in range(1,3):
    url = 'https://bohaishibei.com/post/category/main/page/%d' % page + '/'
    etree = bhsb.perseUrl(url)
    lists = bhsb.bulidlists(etree)
    num = batchsave(lists)
    #images = bhsb.getImage(etree)
   # dowmload = bhsb.downLoadImg(images, page)
    print('插入条数',num)
end=time.strftime("%M:%S")
print(now,':',end)