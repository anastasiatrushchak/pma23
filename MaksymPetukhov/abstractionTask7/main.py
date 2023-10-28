from Red import Red
from Green import Green
from Blue import Blue
from Circle import Circle
from Rectangle import Rectangle
from Square import Square

red = Red()
green = Green()
blue = Blue()

red_circle = Circle(red, 30000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
green_rectangle = Rectangle(green, 2, 4)
blue_square = Square(blue, 5)

print(red_circle, end='\n')
print(green_rectangle, end='\n')
print(blue_square, end='\n')

try:
    wrong = Circle(red, -1)
except ValueError:
    print("Wrong value of radius")

try:
    wrong = Rectangle(red, 0, 4)
except ValueError:
    print("Wrong value of side")

try:
    wrong = Square(red, -1)
except ValueError:
    print("Wrong value of side")