from Circle import Circle
from Rectangle import Rectangle
from Square import Square
from Color import RedColor, GreenColor, BlueColor

red_color = RedColor()
circle = Circle(-5, red_color)

green_color = GreenColor()
rectangle = Rectangle(4, 6, green_color)

blue_color = BlueColor()
square = Square(5, blue_color)

print(f"Circle: Area={circle.area()}, Perimeter={circle.perimeter()}, Color={circle.apply_color()}")
print(f"Rectangle with Green Color: Area={rectangle.area()}, Perimeter={rectangle.perimeter()}, Color={rectangle.apply_color()}")
print(f"Square with Blue Color: Area={square.area()}, Perimeter={square.perimeter()}, Color={square.apply_color()}")
