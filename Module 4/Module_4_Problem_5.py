"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Area of a box
"""


class Box:
    def area(self):
        return self.width * self.height

    def __init__(self, width, height):
        self.width = width
        self.height = height

# Create an instance of Box.
x = Box(37, 21)

# Print area.
print("Area of box 10x2 =", x.area())
