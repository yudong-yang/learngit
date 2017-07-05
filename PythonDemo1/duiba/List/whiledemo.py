'''
Created on 2017年6月7日

@author: Administrator
'''

def  city_country(city,country):
    name = '"'+country+','+city+'"'
    return name

def make_album(singer,album):
    name = '专辑:'+ album + '\t歌手:'+singer
    return name
'''citycon=city_country('hangzhou','china')
print(citycon)

citycon=city_country('shanghai','china')
print(citycon)

citycon=city_country('newyourk','America')
print(citycon)

singeralb = make_album('周杰伦','稻香')
print(singeralb)
singeralb = make_album('刘德华','冰雨')
print(singeralb)
singeralb = make_album('李玉刚','刚好遇见你')
print(singeralb)'''


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    singer = input("输入歌手姓名: ")
    if singer == 'q':
        break
    album = input("输入专辑名称: ")
    if album == 'q':
        break
    formatted_name = make_album(singer,album)
    print("\n歌手专辑列表, " + formatted_name + "!")