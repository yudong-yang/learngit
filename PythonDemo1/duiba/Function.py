'''
Created on 2017年6月2日

@author: Administrator
'''
def greet():
    print('Hello World')

def greet_user(name):
    print('Hello,' , name)
    
def  favorite_book(bookName):
    print(' One of my favorite books is', bookName ,'in Wonderland .')

favorite_book('HisoryBook')


def describe_pet(pet_name='hamster', animal_type='dog'):

    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

def  make_shirt(size, logo):
    print('\nI have a '+size+' T-shirt ,The T-shirt Logo is '+logo)


def  make_shirt_01(size, logo='I Love Python'):
    print('\nI have a '+size+' T-shirt ,The T-shirt Logo is '+logo)


def  make_shirt_02(logo,size='T'):
    print('\nI have a '+size+' T-shirt ,The T-shirt Logo is '+logo)
    
    
def describe_city(city='Hangzhou' , country='China'):
    print(city+' is in '+country+'\n')

make_shirt('M', 'LiNing')

make_shirt_01('S')

make_shirt_02('I Love Huijie')

describe_city()

describe_city('Beijing')

describe_city('Newyork' , 'American')
