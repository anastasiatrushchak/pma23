import abc

class Shape(metaclass=abc.ABCMeta):
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

class ShapeFactory(metaclass=abc.ABCMeta):
    def create_shape(self):
        pass

class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()

class RectangleFactory(ShapeFactory):
    def create_shape(self):
        return Rectangle()

# Client code
if __name__ == "main":
    circle_factory = CircleFactory()
    circle = circle_factory.create_shape()
    circle.draw()

    rectangle_factory = RectangleFactory()
    rectangle = rectangle_factory.create_shape()
    rectangle.draw()