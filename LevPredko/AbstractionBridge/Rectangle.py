from Abstraction import Shape
from abc import ABC, abstractmethod


class Rectangle(Shape, ABC):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def shape_method(self):
        return "\033[1;32mI'm rectangle\033[0m"

    def shape_perimeter(self):
        return 2*(self.width+self.height)

    def shape_area(self):
        return self.height*self.width

