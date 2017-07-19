'''
Created on 2017年6月30日

@author: Administrator
'''
import urllib.request


filename = 'test1.html'

req = urllib.request.Request('')
response = urllib.request.urlopen(req)
the_page = response.read()




with open(filename,'wb+') as file_write:
    file_write.write(the_page)
