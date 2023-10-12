from shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, colour, radius):
        super().__init__(colour)
        self.radius = radius

    def perimetr(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius**2


