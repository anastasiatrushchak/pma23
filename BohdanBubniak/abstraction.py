from abc import ABC, abstractmethod
import math

class Color(ABC):
    @abstractmethod
    def fill_with_color(self):
        pass

class Red(Color):
    def fill_with_color(self):
        return "Red"

class Blue(Color):
    def fill_with_color(self):
        return "Blue"

class Green(Color):
    def fill_with_color(self):
        return "Green"

class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw_shape(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius, color: Color):
        super().__init__(color)
        self.radius = radius

    def draw_shape(self):
        return f"Circle with color {self.color.fill_with_color()}"

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height, color: Color):
        super().__init__(color)
        self.width = width
        self.height = height

    def draw_shape(self):
        return f"Rectangle with color {self.color.fill_with_color()}"

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side, color: Color):
        super().__init__(color)
        self.side = side

    def draw_shape(self):
        return f"Square with color {self.color.fill_with_color()}"

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side ** 2

red_circle = Circle(5, Red())
blue_rectangle = Rectangle(4, 6, Blue())
green_square = Square(3, Green())

print(red_circle.draw_shape(), red_circle.calculate_perimeter(), red_circle.calculate_area())
print(blue_rectangle.draw_shape(), blue_rectangle.calculate_perimeter(), blue_rectangle.calculate_area())
print(green_square.draw_shape(), green_square.calculate_perimeter(), green_square.calculate_area())
