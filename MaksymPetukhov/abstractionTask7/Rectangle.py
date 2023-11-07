from Shape import Shape


class Rectangle(Shape):

    def __init__(self, color, width: float, height: float):
        super().__init__(color)
        if width <= 0 or height <= 0:
            raise ValueError
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_area(self):
        return self.width * self.height
