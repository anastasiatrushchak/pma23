from shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color) #з батьківсського класу взяли конструктор
        if radius <= 0:
            raise ValueError
        self.radius = radius

    def calculate_perim(self):
        return 2*pi*self.radius

    def calculate_square(self):
        return pi*self.radius**2

    def __str__(self):
        return 'Shape: Circle, ' + super().__str__()
