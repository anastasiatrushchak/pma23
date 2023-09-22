from Rectangle import Rectangle
from RostyslavPasternak.Homework.Abstract_class.Color import Color

class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        Rectangle.__init__(self, side, side, color)

    def __str__(self):
        return "Side: " + self.first_side.__str__() + "\nPerimeter: " + self.get_perimeter().__str__() + "\nArea: " + self.get_area().__str__()


square = Square(12)
print(square)
