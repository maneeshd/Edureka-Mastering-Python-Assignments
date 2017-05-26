"""
@author: Maneesh D
@date: May 15, 2017
@interpreter: Python 3.6.1
Dictionary Comprehension
"""
from string import ascii_uppercase


keys = list(ascii_uppercase)
values = list(range(1, 27))
d = {keys[i]: values[i] for i in range(len(keys))}
print(d)
