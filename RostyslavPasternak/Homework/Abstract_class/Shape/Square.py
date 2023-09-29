from Rectangle import Rectangle
from RostyslavPasternak.Homework.Abstract_class.Shape.Colors import *

class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        Rectangle.__init__(self, side, side, color)

    def __str__(self):
        return f"Side: {self.first_side}\nColor: {self.color}\nPerimeter: {self.get_perimeter()}\nArea: {self.get_area()}"
