"""
@author: Maneesh D
@date: 5/26/2017
@intepreter: Python 3.6

Sort a list based on various conditions using operator.itemgetter().
"""
from operator import itemgetter


mylist = [["john", 1, "a"], ["larry", 0, "c"], ["barry", 2, "b"]]
print("-" * 77)
print("Un-Sorted: %s" % mylist)
print("-" * 77)
print("Sorted based on name: %s" % sorted(mylist, key=itemgetter(0)))
print()
print("Sorted based on second element(0/1): %s" % sorted(mylist, key=itemgetter(1)))
print()
print("Sorted based on third element(a/b): %s" % sorted(mylist, key=itemgetter(2)))
print("-" * 77)
