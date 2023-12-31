
class Shape:
    def __init__(self, shape_type, color):
        self.shape_type = shape_type
        self.color = color

    def draw(self):
        return f"Drawing a {self.color} {self.shape_type}"

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__("circle", color)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__("rectangle", color)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def __init__(self, side, color):
        super().__init__("square", color)
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return 4 * self.side


class Color:
    def __init__(self, color_name):
        self.color_name = color_name

    def apply_color(self, shape_type):
        return f"Applying {self.color_name} color to {shape_type}"


red_color = Color("red")
green_color = Color("green")
blue_color = Color("blue")

circle = Circle(5, red_color)
rectangle = Rectangle(4, 6, green_color)
square = Square(3, blue_color)

print(circle.draw())
print(circle.calculate_area())  
print(circle.calculate_perimeter()) 

print(rectangle.draw())  
print(rectangle.calculate_area())  
print(rectangle.calculate_perimeter())  

print(square.draw())  
print(square.calculate_area())  
print(square.calculate_perimeter())  
print(red_color.apply_color("circle"))  
print(green_color.apply_color("rectangle")) 
print(blue_color.apply_color("square")) 