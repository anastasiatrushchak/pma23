from Shape import Shape
from math import pi
from RostyslavPasternak.Homework.Abstract_class.Color import Color
class Circle(Shape):
    def __init__(self,radius: float, color: Color):
        super().__init__(color)
        self.radius = radius

    def __str__(self):
        return "Radius: " + self.radius.__str__() + "\nPerimeter: " + self.get_perimeter().__str__() + "\nArea: " + self.get_area().__str__()
    def get_perimeter(self) -> float:
        return 2 * pi * self.radius
    def get_area(self) -> float:
        return pi * (self.radius ** 2)



circle = Circle(12)
print(circle)