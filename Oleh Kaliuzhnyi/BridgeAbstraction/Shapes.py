from abc import ABC, abstractmethod
from Color import Colors
from math import pi


class __Shape(ABC):
    def __init__(self, color: Colors):
        self.color = color

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Circle(__Shape):
    def __init__(self, color, radius: (int, float)):
        if not isinstance(color, Colors):
            raise ValueError("ValueError! " + color + " color doesn't exist in Color consts!")
        if not isinstance(radius, (int, float)):
            raise TypeError("TypeError! Radius must be numeric type")
        if radius < 0:
            raise ValueError("ValueError! Radius can't be negative")
        if radius == 0:
            raise ValueError("ValueError! Radius can't be zero")
        super().__init__(color)
        self.radius = radius
        self.shape = "circle"

    def get_area(self):
        return self.radius * pi

    def get_perimeter(self):
        return self.radius * 2 * pi

    def __str__(self):
        return ("\nShape is " + self.shape +
                ":\n   Area of " + self.shape + " is " + str(self.get_area()) +
                "\n   Perimeter of " + self.shape + " is " + str(self.get_perimeter()) +
                "\n   Color of " + self.shape + " is " + self.color.get_color())


class Square(__Shape):
    def __init__(self, color, side: (int, float)):
        if not isinstance(color, Colors):
            raise ValueError("ValueError! " + color + " color doesn't exist in Color consts!")
        if not isinstance(side, (int, float)):
            raise TypeError("TypeError! Side must be numeric type")
        if side < 0:
            raise ValueError("ValueError! Side can't be negative")
        if side == 0:
            raise ValueError("ValueError! Side can't be zero")
        super().__init__(color)
        self.side = side
        self.shape = "square"

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return self.side * 4

    def __str__(self):
        return ("\nShape is " + self.shape +
                ":\n   Area of " + self.shape + " is " + str(self.get_area()) +
                "\n   Perimeter of " + self.shape + " is " + str(self.get_perimeter()) +
                "\n   Color of " + self.shape + " is " + self.color.get_color())


class Rectangle(__Shape):
    def __init__(self, color, side_one: (int, float), side_two: (int, float)):
        if not isinstance(color, Colors):
            raise ValueError("ValueError! " + color + " color doesn't exist in Color consts!")
        if not isinstance(side_one, (int, float)) or not isinstance(side_two, (int, float)):
            raise TypeError("TypeError! Side must be numeric type")
        if side_one < 0 or side_two < 0:
            raise ValueError("ValueError! Side can't be negative")
        if side_one == 0 or side_two == 0:
            raise ValueError("ValueError! Side can't be zero")
        super().__init__(color)
        self.side_one = side_one
        self.side_two = side_two
        self.shape = "rectangle"

    def get_area(self):
        return self.side_one * self.side_two

    def get_perimeter(self):
        return (self.side_one + self.side_two) * 2

    def __str__(self):
        return ("\nShape is " + self.shape +
                ":\n   Area of " + self.shape + " is " + str(self.get_area()) +
                "\n   Perimeter of " + self.shape + " is " + str(self.get_perimeter()) +
                "\n   Color of " + self.shape + " is " + self.color.get_color())
