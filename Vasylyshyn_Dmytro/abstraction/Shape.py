from abc import ABC, abstractmethod
from typing import Final
PI: Final[float] = 3.14159265359
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return (
            "\n"
            '----------------------------------------------'
            f"Color: {self.color.apply_color()}\n"
            f"Area: {self.calculate_area()}\n"
            f"Perimeter: {self.calculate_perimeter()}\n"
             '----------------------------------------------'
            "\n"
        )
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        if radius < 0:
            raise ValueError("Radius must be a non-negative number.")
        self.radius = radius
    def calculate_area(self):
        return PI * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * PI * self.radius

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        if width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative numbers.")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length)

    def calculate_area(self):
        return self.width * self.width

    def calculate_perimeter(self):
        return 4 * self.width


