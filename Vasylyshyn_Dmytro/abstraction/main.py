from Vasylyshyn_Dmytro.abstraction.Shape import Circle, Rectangle, Square
from Vasylyshyn_Dmytro.abstraction.colabs import Colabs
from Vasylyshyn_Dmytro.abstraction.color import RedColor, BlueColor, GreenColor

red_circle = Colabs(Circle(RedColor(), 5), RedColor())
print(red_circle.apply_color())  # Output: Circle with Red color

blue_rectangle = Colabs(Rectangle(BlueColor(), 4, 6), BlueColor())
print(blue_rectangle.apply_color())  # Output: Rectangle with Blue color

green_square=Colabs(Square(GreenColor(),4),GreenColor())
print(green_square.apply_color())
print(green_square.get_calculate_area())
print(red_circle)
print(green_square)
print(blue_rectangle)
print(green_square.get_calculate_perimeter())
print(red_circle.get_calculate_perimeter())
