from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area_calculation(self):
        pass

    @abstractmethod
    def per_calculation(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area_calculation(self):
        return self.radius ** 2 * 3.14

    def per_calculation(self):
        return self.radius * 2 * 3.14

    def __str__(self):
        return "Circle"


class Rectangle(Shape):
    def __init__(self, height, width):
        if height < 0 or width < 0:
            raise ValueError("Height and width cannot be negative")
        self.height = height
        self.width = width

    def per_calculation(self):
        return self.height * 2 + self.width * 2

    def area_calculation(self):
        return self.width * self.height

    def __str__(self):
        return "Rectangle"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        if side < 0:
            raise ValueError("Side length cannot be negative")
        self.side = side

    def area_calculation(self):
        return self.side * self.side

    def per_calculation(self):
        return self.side * 4

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


class Purple(Color):
    def __init__(self):
        super().__init__('Purple')

    def get_color(self):
        return super().get_color()

    def color_set(self, color):
        return super().set_color()


class Pink(Color):
    def __init__(self):
        super().__init__('Pink')

    def get_color(self):
        return super().get_color()

    def color_set(self, color):
        return super().set_color()


class Grey(Color):
    def __init__(self):
        super().__init__('Grey')

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
                f" [Area = {self.shape.area_calculation()} Perimeter = {self.shape.per_calculation()}]")


# Example usage:
try:
    first_shape = Rectangle(6, 4)
    first_colour = Grey()
    my_first_shape = Bridge(first_shape, first_colour)
    print(my_first_shape.info())
except ValueError as e:
    print(f"Error: {e}")
