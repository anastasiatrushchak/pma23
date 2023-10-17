from shape_class import Shape
from const import *
class Rectangle(Shape):
    def __init__(self, side_a, side_b, color):
        self.side_a = side_a
        self.side_b = side_b
        super().set_color(color)

    def perimeter(self):
        try:
            if self.side_a > 0 and self.side_b > 0 :
                return 2 * self.side_a + 2 * self.side_b
            else:
                raise Exception("side is negative")
        except:
            print(SIDE_NEG)


    def area(self):
        try:
            if self.side_a > 0 and self.side_b > 0 :
                return self.side_a * self.side_b
            else:
                raise Exception("side is negative")
        except:
            print(SIDE_NEG)



