'''
Created on 2017年6月7日

@author: Administrator
'''
from Dog import *

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
my_dog.roll_over()
my_restaurant = Restaurant('上岛咖啡馆','知名咖啡馆，休闲娱乐的地方')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_car = Car('bmw' , 'x6' ,'2016')
ben_car = Car('Benchi' ,'a8' ,'2017')
desc = my_car.car_descrption()
print(desc)
my_car.car_start()
my_car.car_stop()
my_car.read_odometer()
my_car.update_odometer(100)
my_car.update_odometer(100)
ben_car.read_odometer()
my_car.fill_gas_tank()

elec_car = ElectricCar('dazhong','toyota','2017',10)
elecar = elec_car.car_descrption()
print(elecar)
elec_car.charge_electric(4)
elec_car.battery.describe_battery()

ranges = elec_car.battery.get_range()
print(ranges)