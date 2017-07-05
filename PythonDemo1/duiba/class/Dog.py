'''
Created on 2017年6月7日

@author: Administrator
'''

class Dog(object):

    def __init__(self, name,age):
        '''
        Constructor
        '''
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now sitting.")
        
    def  roll_over(self):
        """ 模拟小狗被命令时打滚 """
        print(self.name.title() + " rolled over!")
        

class Restaurant():
    '创建restaurant 实体类，包含餐馆名称和描述'
    
    def __init__(self, restaurant_name,cuisine_type):
        '''
                            构造函数
        '''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print('餐馆名称是：'+ self.restaurant_name+',餐馆的类型是：'+self.cuisine_type)
    
    def open_restaurant(self):
        print(self.restaurant_name+' 正在营业，欢迎光临！ ')
        
        
class Car():
    '创建汽车的简单实体类和方法'
    def __init__(self, name, ctype, year):
        self.name=name
        self.ctype = ctype
        self.year = year
        self.odometer_reading=0
    def car_descrption(self):
        descrption='The car name is '+self.name + ' its type is '+ self.ctype+' made in '+self.year + ' year !'
        return descrption
    
    def car_start(self):
        print('The car '+self.name+' fire ,the car run !')
    
    def car_stop(self):
        print(('The car '+self.name+' power off ,the car stop !'))
    
    def read_odometer(self):
        """ 打印一条指出汽车里程的消息 """
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self,malemeter):
        if malemeter>=0:
            self.odometer_reading = self.odometer_reading + malemeter
            print("This car "+self.name+" has " + str(self.odometer_reading) + " miles on it.")
        elif malemeter>200000:
            print("Your car has been scrapped !")
        else:
            print("Your input was wrong !")
    def fill_gas_tank(self):
        "电车没有油箱"
        print("This car need a gas tank!")
    
class ElectricCar(Car):
    "继承Car的ElectricCar"
    def __init__(self,make, model, year,battery_size=100):
        super().__init__(make, model, year)
        self.battery = Battery(battery_size) 
        
    def charge_electric(self,hours):
        "需要充电的时间"
        print(self.name+" need charge for "+str(hours)+" hours electricity")
    
    def fill_gas_tank(self):
        "电车没有油箱"
        print("This car doesn't need a gas tank!")
        
        
class Battery():
    
    def __init__(self,battery_size=70):
        
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+ " -kWh battery.")
        
    def get_range(self):
        if self.battery_size>200:
            message = "Input wrong number ! "
        elif self.battery_size > 40:
            ranges = self.battery_size*2 + 100
            message = "This car can go approximately " + str(ranges)
        else:
            message = "This car is low power ! "
        return message
    
    
    