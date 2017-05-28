"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Script Corection: [Expected output: x-value: 5 y-value: 7]
"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x-value: " + str(self.x) + " y-value: " + str(self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(3, 4)
p2 = Point(2, 3)
print(p1 + p2)
