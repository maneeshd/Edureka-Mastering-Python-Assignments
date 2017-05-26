"""
@author: Maneesh D
@date: May 15, 2017
@interpreter: Python 3.6.1
Reverse/Inverse a Dictionary
"""
dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
dict2 = dict(zip(dict1.values(), dict1.keys()))
print(dict2)
