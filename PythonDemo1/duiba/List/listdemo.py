'''
Created on 2017年6月6日

@author: Administrator
'''
friends = ['zhangsan','lisi','wangwu','zhaoliu']

def replaces(lists, tag1, tag2):
    index = lists.index(tag1)
    lists.remove(tag1)
    lists.insert(index, tag2)
    
def greet(friends):
    for friend in friends:
        print('Welcome to my Party for you '+friend)

def del_friends(friends):
    n=len(friends)
    while n>2:
        name = friends.pop()
        print('I\'m sorry for you leave My party '+name)
        n=n-1
 
replaces(friends,'zhangsan' , 'zhangxiaosan')
middle = int(len(friends)/2)
friends.insert(middle, 'xiaowang')
friends.append('sunxinlong')
print('排序前 :') 
print(friends)
friends.sort(key=None, reverse=True)
print('排序后 :')
print(friends)
del_friends(friends)
greet(friends)

friends.pop(1)
friends.pop(0)