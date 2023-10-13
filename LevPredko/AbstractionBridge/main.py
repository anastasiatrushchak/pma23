from ImitativeClasses import RedColor, BlueColor, YellowColor, Circle, Rectangle, Square


def print_shape_info(shape):
    if isinstance(shape, Circle):
        print(f"{shape.shape_method()}")
        print(f"Color: {shape.color.shape_color()}")
        print(f"Radius: {shape.radius}")
        print(f"Perimeter: {shape.shape_perimeter()}")
        print(f"Area: {shape.shape_area()}")
    elif isinstance(shape, Rectangle):
        print(f"{shape.shape_method()}")
        print(f"Color: {shape.color.shape_color()}")
        print(f"Width: {shape.width}")
        print(f"Height: {shape.height}")
        print(f"Perimeter: {shape.shape_perimeter()}")
        print(f"Area: {shape.shape_area()}")
    elif isinstance(shape, Square):
        print(f"{shape.shape_method()}")
        print(f"Color: {shape.color.shape_color()}")
        print(f"Side: {shape.side}")
        print(f"Perimeter: {shape.shape_perimeter()}")
        print(f"Area: {shape.shape_area()}")
    else:
        print("Unknown shape")


circle = Circle(5, RedColor())
rectangle = Rectangle(4, 6, BlueColor())
square = Square(3, YellowColor())

print_shape_info(circle)
print("-------------")
print_shape_info(rectangle)
print("-------------")
print_shape_info(square)