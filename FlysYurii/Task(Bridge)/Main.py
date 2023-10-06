from Circle import Circle
from Rectangle import Rectangle
from Square import Square
from Color import Red,Green,Blue
red = Red()
green = Green()
blue = Blue()

circle = Circle(5, red)
print(f"Коло: Площа = {circle.calculate_area()}, Периметр = {circle.calculate_perimeter()}, Колір = {circle.color.fill_color()}")

rectangle = Rectangle(4, 3, green)
print(f"Прямокутник: Площа = {rectangle.calculate_area()}, Периметр = {rectangle.calculate_perimeter()}, Колір = {rectangle.color.fill_color()}")

square = Square(4, blue)
print(f"Квадрат: Площа = {square.calculate_area()}, Периметр = {square.calculate_perimeter()}, Колір = {square.color.fill_color()}")