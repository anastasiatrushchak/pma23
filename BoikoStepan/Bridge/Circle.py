from Shape import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def apply_color(self):
        return self.color.apply_color()
