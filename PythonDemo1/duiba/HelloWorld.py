'''
Created on 2017年6月1日

@author: Administrator
'''
i=1
print("Hello world %d" % i)

def power(x, n=2):##默认的N=2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5,3))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

val = calc(1, 3, 5, 7)

print(val)


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
fact = fact(100)
print("15 的阶乘是 %d" % fact)

def move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
        return
    move(n-1,a,c,b)
    move(1,a,b,c)
    move(n-1,b,a,c)
    
print(move(2, 'a' ,'b', 'c'))



