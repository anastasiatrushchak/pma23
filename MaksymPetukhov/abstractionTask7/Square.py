from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return 4 * self.side
