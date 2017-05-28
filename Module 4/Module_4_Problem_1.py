"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Regular Expression that will match a date that follows the standard:- "YYYY-MM-DD"
"""
from datetime import date
from re import compile

pattern = compile("\d{4}-\d{2}-\d{2}")
today = date.today().strftime("%Y-%m-%d")

if pattern.search(today):
    print("Date is in 'YYYY-MM-DD' format: %s" % today)
else:
    print("Not a 'YYYY-MM-DD' Date Match for %s" % today)

invalid = "123-456-7"
if pattern.search(invalid):
    print("Date is in 'YYYY-MM-DD' format: %s" % invalid)
else:
    print("Not a 'YYYY-MM-DD' Date Match for %s" % invalid)

test_str = """
            fsf2010-08-27sdfsdfsd
            dsf sfds f2010-08-26 fsdf 
            asdsds 2009-02-02 afdf
           """

print(pattern.findall(test_str))
