


def sublist(lists1 , lists2):
    sublist = []
    for b in lists1:
        if b[0] in lists2:
            sublist.append(b)
    for i in sublist:
        lists1.remove(i)
    return lists1
list1 = [(1,2),(2,3),(3,4)]
list2 = [ 1,3]
print(list1)

lists2 = sublist(list1,list2)
print(lists2)


