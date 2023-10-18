from figures import Circle, Rectangle, Square
from colors import YellowColor, GreenColor, RedColor

yellow = YellowColor()
green = GreenColor()
red = RedColor()

circle = Circle(6, yellow)
print(circle.draw())
print(f"Периметр: {circle.get_perimeter()}")
print(f"Площа: {circle.get_area()}")

rectangle = Rectangle(4, 6, green)
print(rectangle.draw())
print(f"Периметр: {rectangle.get_perimeter()}")
print(f"Площа: {rectangle.get_area()}")

square = Square(3, red)
print(square.draw())
print(f"Периметр: {square.get_perimeter()}")
print(f"Площа: {square.get_area()}")
