from shape_class import Shape
from const import  *
class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        super().set_color(color)

    def perimeter(self):
        try:
            if self.side > 0 :
                return 4 * self.side
            else:
                raise Exception("side is negative")
        except:
            print(SIDE_NEG)


    def area(self):
        try:
            if self.side > 0 :
                return self.side**2
            else:
                raise Exception("side is negative")
        except:
            print(SIDE_NEG)



