from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, width, color):
        super().__init__(width, width, color)
        self.width = width
        self.color = color

    def area(self):
        return self.width ** 2

    def perimeter(self):
        return 4 * self.width

    def apply_color(self):
        return self.color.apply_color()
