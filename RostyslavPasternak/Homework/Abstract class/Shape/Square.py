from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side: float):
        Rectangle.__init__(self, side, side)

    def __str__(self):
        return "Side: " + self.first_side.__str__() + "\nPerimeter: " + self.get_perimeter().__str__() + "\nArea: " + self.get_area().__str__()


square = Square(12)
print(square)
