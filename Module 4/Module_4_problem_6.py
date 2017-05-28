"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Distance between two points using class.
"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, point):
        x_part = (self.x - point.x) ** 2
        y_part = (self.y - point.y) ** 2
        return (x_part + y_part) ** 0.5

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

point1 = Point(2, 5)
point2 = Point(7, 10)
print("Distance between %s and %s = %.2f" % (point1, point2, point1.distance(point2)))
