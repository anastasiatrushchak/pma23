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


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        try:
            if self.radius < 0:
                raise ValueError("Radius cannot be negative")
            return self.radius ** 2 * 3.14
        except ValueError as e:
            return str(e)

    def calculate_perimeter(self):
        try:
            if self.radius < 0:
                raise ValueError("Radius cannot be negative")
            return 2 * 3.14 * self.radius
        except ValueError as e:
            return str(e)

    def __str__(self):
        return "Circle"


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        try:
            if self.height < 0 or self.width < 0:
                raise ValueError("Height and width cannot be negative")
            return self.height * 2 + self.width * 2
        except ValueError as e:
            return str(e)

    def calculate_area(self):
        try:
            if self.height < 0 or self.width < 0:
                raise ValueError("Height and width cannot be negative")
            return self.width * self.height
        except ValueError as e:
            return str(e)

    def __str__(self):
        return "Rectangle"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def calculate_area(self):
        try:
            if self.side < 0:
                raise ValueError("Side length cannot be negative")
            return self.side ** 2
        except ValueError as e:
            return str(e)

    def calculate_perimeter(self):
        try:
            if self.side < 0:
                raise ValueError("Side length cannot be negative")
            return self.side * 4
        except ValueError as e:
            return str(e)

    def __str__(self):
        return "Square"


class Color(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_color(self):
        return self.color

    @abstractmethod
    def color_set(self, color):
        self.color = color


class Green(Color):
    def __init__(self):
        super().__init__('Green')

    def get_color(self):
        return super().get_color()

    def color_set(self, color):
        return super().set_color()


class White(Color):
    def __init__(self):
        super().__init__('White')

    def get_color(self):
        return super().get_color()

    def color_set(self, color):
        return super().set_color()


class Purple(Color):
    def __init__(self):
        super().__init__('Purple')

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


square = Square(-9)
green = Green()
green_square = Bridge(square, green)

rectangle = Rectangle(5, 9)
white = White()
white_rectangle = Bridge(rectangle, white)

circle = Circle(7)
purple = Purple()
purple_circle= Bridge(circle, purple)

print(green_square.info())
print(white_rectangle.info())
print(purple_circle.info())