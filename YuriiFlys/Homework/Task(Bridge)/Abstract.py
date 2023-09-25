from abc import ABC, abstractmethod
from math import pi

class Color(ABC):
    @abstractmethod
    def fill_color(self):
        pass

class Red(Color):
    def fill_color(self):
        return "Червоний"

class Green(Color):
    def fill_color(self):
        return "Зелений"

class Blue(Color):
    def fill_color(self):
        return "Синій"

class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side

red = Red()
green = Green()
blue = Blue()

circle = Circle(5, red)
print(f"Коло: Площа = {circle.calculate_area()}, Периметр = {circle.calculate_perimeter()}, Колір = {circle.color.fill_color()}")

rectangle = Rectangle(4, 3, green)
print(f"Прямокутник: Площа = {rectangle.calculate_area()}, Периметр = {rectangle.calculate_perimeter()}, Колір = {rectangle.color.fill_color()}")

square = Square(4, blue)
print(f"Квадрат: Площа = {square.calculate_area()}, Периметр = {square.calculate_perimeter()}, Колір = {square.color.fill_color()}")