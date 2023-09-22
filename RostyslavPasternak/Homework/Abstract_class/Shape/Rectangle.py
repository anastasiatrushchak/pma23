from Shape import Shape
from RostyslavPasternak.Homework.Abstract_class.Color import Color

class Rectangle(Shape):
    def __init__(self, first_side: (float, int), second_side: (float, int), color: Color):
        super().__init__(color)
        self.first_side = first_side
        self.second_side = second_side
    def __str__(self)-> str:
        return "Side: " + self.first_side.__str__()+" and "+self.second_side.__str__() + "\nPerimeter: " + self.get_perimeter().__str__() + "\nArea: " + self.get_area().__str__();

    def get_perimeter(self) -> float:
        return (2 * self.first_side) + (2 * self.second_side)

    def get_area(self) -> float:
        return self.first_side * self.second_side


rectangle = Rectangle(12, 2)
print(rectangle)