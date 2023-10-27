from Rectangle import Rectangle
from Square import Square
from Circle import Circle
from Red import Red
from Blue import Blue
from Yellow import Yellow

red = Red()
blue = Blue()
yellow = Yellow()
try:
    rectangle = Rectangle(red, 5, 7)
    print(rectangle)
except ValueError:
    print("Value cannot be negative")
try:
    circle = Circle(blue, 5)
    print(circle)
except ValueError:
    print("Value cannot be negative")
try:
    square = Square(yellow, 8)
    print(square)
except ValueError:
    print("Value cannot be negative")
