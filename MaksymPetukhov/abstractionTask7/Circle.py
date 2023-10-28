from Shape import Shape
from math import pi


class Circle(Shape):

    def __init__(self, color, radius: float):
        super().__init__(color)
        if radius <= 0:
            raise ValueError
        self.radius = radius

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_area(self):
        return pi * self.radius ** 2
