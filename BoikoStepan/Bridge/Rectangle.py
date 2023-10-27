from Shape import Figure


class Rectangle(Figure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def apply_color(self):
        return self.color.apply_color()
