from circle import Circle
from square import Square
from rectangle import Rectangle
from red import Red
from green import Green
from blue import Blue

circle = Circle(Red(), 5)
square = Square(Green(), 3)
rectangle = Rectangle(Blue(), 10, 5)
print(circle.area())
print(square.perimetr())
rectangle.paint()



