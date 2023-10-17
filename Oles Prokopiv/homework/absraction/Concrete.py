from abstractclass import Shape, Color

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


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return self.side * 4

    def __str__(self):
        return "Square"

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

