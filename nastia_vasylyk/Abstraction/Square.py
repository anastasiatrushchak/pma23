from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, color, a):
        super().__init__(color, a, a)
        if a <= 0:
            raise ValueError

    def __str__(self):
            return 'Shape: Square, ' + super().__str__()