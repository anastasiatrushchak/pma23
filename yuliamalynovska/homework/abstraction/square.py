from shape import Shape


class Square(Shape):
    def __init__(self, colour, side):
        super().__init__(colour)
        self.side = side

    def perimetr(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

