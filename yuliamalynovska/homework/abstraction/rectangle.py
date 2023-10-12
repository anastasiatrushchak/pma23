from shape import Shape


class Rectangle(Shape):
    def __init__(self, colour, side1, side2):
        super().__init__(colour)
        self.side1 = side1
        self.side2 = side2

    def perimetr(self):
        return 2 * (self.side1 + self.side2)

    def area(self):
        return self.side1 * self.side2


