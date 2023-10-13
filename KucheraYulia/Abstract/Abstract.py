from abc import ABC


class Figure(ABC):
    def __init__(self, color):
        self.color = color

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Color(ABC):
    def __init__(self, name):
        self.name = name


class RedColor(Color):
    def __init__(self):
        super().__init__("Red")


class GreenColor(Color):
    def __init__(self):
        super().__init__("Green")


class BlueColor(Color):
    def __init__(self):
        super().__init__("Blue")


class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Figure):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Square(Figure):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

    def calculate_perimeter(self):
        return 4 * self.side_length


red = RedColor()
green = GreenColor()

circle = Circle(red, 5)
print(f"Circle area: {circle.calculate_area()}, perimeter: {circle.calculate_perimeter()}, color: {circle.color.name}")

square = Square(green, 4)
print(f"Square area: {square.calculate_area()}, perimeter: {square.calculate_perimeter()}, color: {square.color.name}")
