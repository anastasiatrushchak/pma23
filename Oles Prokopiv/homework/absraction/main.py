from Concrete import Circle, Rectangle, Square, Yellow, Blue, Red

class Bridge:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def info(self):
        return (f"{self.color.get_color()} {self.shape}"
                f" [Area = {self.shape.calculate_area()} Perimeter = {self.shape.calculate_perimeter()}]")


sq = Square(-5)
bl = Blue()
blue_square = Bridge(sq, bl)

rect = Rectangle(4, 6)
yell = Yellow()
yellow_rectangle = Bridge(rect, yell)


print(blue_square.info())
print(yellow_rectangle.info())
