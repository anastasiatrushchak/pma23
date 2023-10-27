from shape import Shape


class Rectangle(Shape):
    def __init__(self, color, a, b ):
        super().__init__(color)
        if a <= 0 or b <= 0:
            raise ValueError
        self.a = a
        self.b = b

    def calculate_perim(self):
        return 2*self.a*2*self.b

    def calculate_square(self):
        return self.a*self.b

    def __str__(self):
        return 'Shape: Rectangle, ' + super().__str__()