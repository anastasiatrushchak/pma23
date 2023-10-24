from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)
        self.side = side
    def shape_method(self):
        return "\033[1;32mI'm square\033[0m"

    def shape_perimeter(self):
        return 4 * self.side

    def shape_area(self):
        return pow(self.side, 2)