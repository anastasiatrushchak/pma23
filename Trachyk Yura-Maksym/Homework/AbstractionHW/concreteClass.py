from abstractClass import Shape, Color

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = self.radius ** 2 * 3.14
        if area < 0:
            print("Площа не може бути від'ємною. Будь ласка, введіть додатне число.")
            return 0
        return area

    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        if perimeter < 0:
            print("Периметр не може бути від'ємним. Будь ласка, введіть додатне число.")
            return 0
        return perimeter

    def __str__(self):
        return "Circle"


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        perimeter = self.height * 2 + self.width * 2
        if perimeter < 0:
            print("Периметр не може бути від'ємним. Будь ласка, введіть додатне число.")
            return 0
        return perimeter

    def calculate_area(self):
        area = self.width * self.height
        if area < 0:
            print("Площа не може бути від'ємною. Будь ласка, введіть додатне число.")
            return 0
        return area

    def __str__(self):
        return "Rectangle"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def calculate_area(self):
        area = self.side ** 2
        if area < 0:
            print("Площа не може бути від'ємною. Будь ласка, введіть додатне число.")
            return 0
        return area

    def calculate_perimeter(self):
        perimeter = self.side * 4
        if perimeter < 0:
            print("Периметр не може бути від'ємним. Будь ласка, введіть додатне число.")
            return 0
        return perimeter

    def __str__(self):
        return "Square"


class Color:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


class Red(Color):
    def __init__(self):
        super().__init__('Red')

    def get_color(self):
        return super().get_color()

    def set_color(self, color):
        return super().set_color(color)


class Blue(Color):
    def __init__(self):
        super().__init__('Blue')

    def get_color(self):
        return super().get_color()

    def set_color(self, color):
        return super().set_color(color)


class Yellow(Color):
    def __init__(self):
        super().__init__('Yellow')

    def get_color(self):
        return super().get_color()

    def set_color(self, color):
        return super().set_color(color)

