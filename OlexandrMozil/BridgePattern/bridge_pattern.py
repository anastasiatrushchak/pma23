from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return self.side * 4

    def __str__(self):
        return "Square"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** self.radius * 3.14

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def __str__(self):
        return "Circle"


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return self.height * 2 + self.width * 2

    def calculate_area(self):
        return self.width * self.height

    def __str__(self):
        return "Rectangle"


class Color(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_color(self):
        return self.color

    @abstractmethod
    def color_set(self, color):
        self.color = color


class Red(Color):
    def __init__(self):
        super().__init__('Red')

    def get_color(self):
        return super().get_color()

    def color_set(self, color):
        return super().set_color()


class Blue(Color):
    def __init__(self):
        super().__init__('Blue')

    def get_color(self):
        return super().get_color()

    def color_set(self, color):
        return super().set_color()


class Yellow(Color):
    def __init__(self):
        super().__init__('Yellow')

    def get_color(self):
        return super().get_color()

    def color_set(self, color):
        return super().set_color()


class Bridge:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def info(self):
        return (f"{self.color.get_color()} {self.shape}"
                f" [Area = {self.shape.calculate_area()} Perimeter = {self.shape.calculate_perimeter()}]")


sq = Square(5)
bl = Blue()
red_square = Bridge(sq, bl)

rect = Rectangle(4, 6)
yell = Yellow()
yellow_rectangle = Bridge(rect, yell)


print(red_square.info())
print(yellow_rectangle.info())
