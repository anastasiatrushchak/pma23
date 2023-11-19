from Color import RED, BLACK, WHITE
from Shapes import Circle, Rectangle, Square

try:
    circle = Circle(RED, 1)
    print(circle)
    rectangle = Rectangle(WHITE, 3, 4)
    print(rectangle)
    square = Square(BLACK, 6)
    print(square)
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)
except NameError as err:
    print(err)
