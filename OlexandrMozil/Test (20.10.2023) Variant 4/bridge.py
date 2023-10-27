from abc import ABC


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass


class Rect(Shape):
    def __init__(self, side1, side2, color):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * (self.side1 + self.side2)

    def draw(self):
        return f"Side1: {self.side1}, Side2: {self.side2}, Color: {self.color}, Area: {self.area()}, Perimeter: {self.perimeter()}"


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def draw(self):
        return f"Radius: {self.radius}, Color: {self.color}, Area: {self.area()}, Perimeter: {self.perimeter()}"


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def draw(self):
        return f"Side: {self.side}, Color: {self.color}, Area: {self.area()}, Perimeter: {self.perimeter()}"


class Color(ABC):
    def __init__(self, color):
        self.color = color

    def paint(self):
        pass

    def __str__(self):
        return self.color


class Red(Color):
    def __init__(self):
        super().__init__("Red")

    def paint(self):
        return "Red"


class Blue(Color):
    def __init__(self):
        super().__init__("Blue")

    def paint(self):
        return "Blue"


class Bridge:
    def __init__(self, shape: Shape, color: Color):
        self.color = color
        self.shape = shape

    def draw(self):
        print(self.shape.draw())
        print(self.color.paint())


color_red = Red()
color_blue = Blue()
shape_rect = Rect(5, 10, color_red)
shape_circle = Circle(5, color_blue)
shape_square = Square(5, color_red)
bridge_rect = Bridge(shape_rect, color_red)
bridge_rect.draw()
