"""
@author: Maneesh D
@date: 5/26/2017
@intepreter: Python 3.6

Sort a list based on various conditions using lambda functions.
"""
mylist = [["john", 1, "a"], ["larry", 0, "c"], ["barry", 2, "b"]]
print("-" * 77)
print("Un-Sorted: %s" % mylist)
print("-" * 77)
print("Sorted based on name: %s" % sorted(mylist, key=lambda l: l[0]))
print("Sorted based on second element(0/1): %s" % sorted(mylist, key=lambda l: l[1]))
print("Sorted based on third element(a/b): %s" % sorted(mylist, key=lambda l: l[2]))
print("-" * 77)
