from Shape import Shape
from math import pi
class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.radius