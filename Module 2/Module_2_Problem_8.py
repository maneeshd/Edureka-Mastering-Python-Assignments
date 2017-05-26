"""
@author: Maneesh D
@date: May 15, 2017
@interpreter: Python 3.6.1
"""
L = ['a', 'b', 'c', 'd']
d = dict()
for value, key in enumerate(L):
    d[key] = (value + 1)
print(d)
