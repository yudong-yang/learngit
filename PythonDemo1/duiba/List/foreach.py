'''
Created on 2017年6月6日

@author: Administrator
'''
"""n=1
for cat in  range(1,10):
    for dog in  range(1,n+1):
        sum = cat*dog
        print('%d x %d = %d' % (dog,cat,sum),end='\t' )
    n=n+1
    print('')"""


    
nums = []
lists = list( range(0,30,3))

for num in lists:
    print(num)

squares = [value**3 for value in range(1,11)]
print(squares)