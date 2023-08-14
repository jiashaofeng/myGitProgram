# -*- coding: UTF-8 -*-
# import requests
#
# print('a')
import json
a={'a':1, 'b':'2', 'c':'3'}
# d=a.pop('a')
# print(d)  1
del a['a']
print(a)

dict1 = {'name':'张三','number':'1371','age': 21}

dict2 =json.dumps(dict1)
print(dict2)
dict3=json.loads(dict2)
print(type(dict2))
print(type(dict3))
