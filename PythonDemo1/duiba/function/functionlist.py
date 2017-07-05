'''
Created on 2017年6月7日

@author: Administrator
'''
def build_profile(first, last, **user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key ,value in user_info.items():
        profile[key] = value
    return profile

def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
