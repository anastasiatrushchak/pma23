from Abstraction import Color, Shape


class RedColor(Color):
    def shape_color(self):
        return "Red"


class BlueColor(Color):
    def shape_color(self):
        return "Blue"


class YellowColor(Color):
    def shape_color(self):
        return "Yellow"


class Circle(Shape):

    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def shape_method(self):
        return "\033[1;32mI'm circle\033[0m"

    def shape_perimeter(self):
        return 3.14159265358979*self.radius*2

    def shape_area(self):
        return 3.14159265358979*pow(self.radius, 2)


class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def shape_method(self):
        return "\033[1;32mI'm rectangle\033[0m"

    def shape_perimeter(self):
        return 2*(self.width+self.height)

    def shape_area(self):
        return self.height*self.width


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def shape_method(self):
        return "\033[1;32mI'm square\033[0m"

    def shape_perimeter(self):
        return 4*self.side

    def shape_area(self):
        return pow(self.side, 2)
