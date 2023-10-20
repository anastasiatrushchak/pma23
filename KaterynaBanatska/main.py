
import abc

class Shape(metaclass=abc.ABCMeta):
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

    def perim(self):
        pass

    def area(self):
        pass


class Color(metaclass=abc.ABCMeta):

    def fill(self):
        pass


class Blue(Color):
    def fill(self):
        return "blue"


class Red(Color):
    def fill(self):
        return "red"





class Rectangle(Shape):
    def __init__(self, color, side_a, side_b):
        super().__init__(color)
        self.side_a = side_a
        self.side_b = side_b

    def draw(self):
        return f"This rectangle is {self.color.fill()}"

    def perim(self):
        try:
            if self.side_a <= 0 or self.side_b <= 0:
                raise ValueError("Side length must be a positive number")
            return (self.side_a + self.side_b) * 2
        except ValueError as e:
            return f"Error: {e}"

    def area(self):
        try:
            if self.side_a <= 0 or self.side_b <= 0:
                raise ValueError("Side length must be a positive number")
            return self.side_a * self.side_b
        except ValueError as e:
            return f"Error: {e}"

class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color,side,side)
        self.side = side

    def draw(self):
        return f"This square is {self.color.fill()}"

    def perim(self):
        try:
            if self.side <= 0:
                raise ValueError("Side length must be a positive number")
            return self.side * 4
        except ValueError as e:
            return f"Error: {e}"

    def area(self):
        try:
            if self.side <= 0:
                raise ValueError("Side length must be a positive number")
            return self.side
        except ValueError as e:
            return f"Error: {e}"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        return f"This circle is {self.color.fill()}"

    def perim(self):
        try:
            if self.radius <= 0:
                raise ValueError("Radius must be a positive number")
            return 3.14 * self.radius * 2
        except ValueError as e:
            return f"Error: {e}"

    def area(self):
        try:
            if self.radius <= 0:
                raise ValueError("Radius must be a positive number")
            return 3.14 * (self.radius)
        except ValueError as e:
            return f"Error: {e}"


blue_color = Blue()
red_color = Red()

square = Square(blue_color, 4)
circle = Circle(red_color, 3)

print(square.draw())
print(square.area())
print(square.perim())

print(circle.draw())
print(circle.area())
print(circle.perim())