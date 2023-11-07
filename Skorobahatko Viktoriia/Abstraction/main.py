import abc
import math
pi = math.pi

class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return f'{self.color.fill()}'

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Color(metaclass=abc.ABCMeta):
    def fill(self):
        pass

class RedColor(Color):
    def fill(self):
        return "red"

class GreenColor(Color):
    def fill(self):
        return "green"

class BlueColor(Color):
    def fill(self):
        return "blue"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        try:
            if self.radius < 0:
                raise ValueError ("Radius must be non-negative")
            return pi * self.radius * self.radius
        except ValueError as e:
            return f"Error: {e}"

    def calculate_perimeter(self):
        try:
            if self.radius < 0:
                raise ValueError("Radius must be non-negative")
            return 2 * pi * self.radius
        except ValueError as e:
            return f'Error: {e}'

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        try:
            if self.width < 0 or self.length < 0:
                raise ValueError ("Width and lenght must be non-negative")
            return self.length * self.width
        except ValueError as e:
            return f"Error: {e}"

    def calculate_perimeter(self):
        try:
            if self.width < 0 or self.length < 0:
                raise ValueError ("Width and lenght must be non-negative")
            return 2 * (self.length + self.width)
        except ValueError as e:
            return f"Error: {e}"
class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def calculate_area(self):
        try:
            if self.side_length < 0:
                raise ValueError ("Width and lenght must be non-negative")
            return self.side_length ** 2
        except ValueError as e:
            return f"Error: {e}"
    def calculate_perimeter(self):
        try:
            if self.side_length < 0:
                raise ValueError ("Width and lenght must be non-negative")
            return 4 * self.side_length
        except ValueError as e:
            return f"Error: {e}"

if __name__ == "__main__":
    red_color = RedColor()
    green_color = GreenColor()
    blue_color = BlueColor()

    circle = Circle(red_color, 5)
    rectangle = Rectangle(green_color, 4, 6)
    square = Square(blue_color, 3)

    print("Circle - Color:", circle.get_color(), "Area:", circle.calculate_area(), "Perimeter:", circle.calculate_perimeter())
    print("Rectangle - Color:", rectangle.get_color(), "Area:", rectangle.calculate_area(), "Perimeter:", rectangle.calculate_perimeter())
    print("Square - Color:", square.get_color(), "Area:", square.calculate_area(), "Perimeter:", square.calculate_perimeter())
