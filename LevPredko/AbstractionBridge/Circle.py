from Abstraction import Shape


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

