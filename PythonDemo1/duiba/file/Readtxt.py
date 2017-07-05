'''
Created on 2017年6月8日

@author: Administrator
'''
filename = 'pi_digits.txt'
copytext = 'copytext.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    print(pi_string[2:50]+'...')
    print(len(pi_string))
    
with open(filename,'w') as file_write:
    file_write.write(pi_string)
