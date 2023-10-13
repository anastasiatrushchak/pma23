from const import *
from shape_class import Shape

class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        super().set_color(color)

    def perimeter(self):
        try:
            if self.radius > 0:
                return 2 * PI * self.radius
            else:
                raise Exception("side is negative")
        except:
            print(RAD_NEG)


    def area(self):
        try:
            if self.radius > 0:
                return PI * (self.radius**2)
            else:
                raise Exception
        except:
            print(RAD_NEG)





