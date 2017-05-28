"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Regular Expression that will match a traditional SSN.
"""
from re import compile


pattern = compile("^\d{3}-\d{2}-\d{4}$")

ssn_list = ["234-56-5924", "12-5-78912", "123-5-7891", "1123-56-7777", "006-07-0001"]

for ssn in ssn_list:
    if pattern.match(ssn):
        print("%s is a valid SSN." % ssn)
    else:
        print("%s is an invalid SSN." % ssn)
