from Shape import Shape

class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side