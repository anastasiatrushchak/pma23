from Shape import Shape
from math import pi
from RostyslavPasternak.Homework.Abstract_class.Shape.Colors import *
class Circle(Shape):
    def __init__(self,radius: float, color: Color):
        super().__init__(color)
        self.radius = radius

    def __str__(self):
        return f"Radius: {self.radius}\nColor: {self.color}\nPerimeter: {self.get_perimeter()}\nArea: {self.get_area()}"
    def get_perimeter(self) -> float:
        return 2 * pi * self.radius
    def get_area(self) -> float:
        return pi * (self.radius ** 2)

