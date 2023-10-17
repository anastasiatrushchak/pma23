from abc import ABC, abstractmethod


class Shape(ABC):
    def set_color(self, color):
        self.color = color.color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'Shape: {type(self).__name__}, Color: {self.color}, Area: {self.area()}, Perimetr: {self.perimeter()}'
