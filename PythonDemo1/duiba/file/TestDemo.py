'''
Created on 2017年6月8日

@author: Administrator
'''

guest='guest.txt'
guest_book='guest_book.txt'


'输入姓名，存储到guest中'


name = ''
n=1
while name!='q':
    name=input('输入与会者名单：')
    with open(guest, 'a') as fw:
        if name!='q':
            fw.write('你好'+str(name)+'你是第 '+str(n)+'名嘉宾 ，欢迎光临 ! \n')
    print(name)
    n=n+1



with open(guest) as fw:
    lines = fw.readlines()
    for line in lines:
        print(line.rstrip()) #rstrip() 去掉行内空格    