from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return 4 * self.side