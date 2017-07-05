'''
Created on 2017年6月1日

@author: Administrator
'''
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
        
stus = Student('xiaom',16)

battery_size=70
charges = battery_size*2 + 100
print(charges)