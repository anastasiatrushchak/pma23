from RostyslavPasternak.Homework.Abstract_class.Shape.Colors import *
from Shape import Shape


class Rectangle(Shape):
    def __init__(self, first_side: (float,int), second_side: (float,int), color: Color):
        super().__init__(color)
        self.first_side = first_side
        self.second_side = second_side
    def __str__(self):

        # return "Sides: " + str(self.first_side) + " and " + str(self.second_side) + "\nColor: " + str(
        #     self.color) + "\nPerimeter: " + str(self.get_perimeter()) + "\nArea: " + str(self.get_area())
        # return f"""
        # Sides: {self.first_side} and {self.second_side}
        # Color: {self.color}
        # Perimeter: {self.get_perimeter()}
        # Area: {self.get_area()}
        # """
        return f"Side: {self.first_side} and {self.second_side}\nColor: {self.color}\nPerimeter: {self.get_perimeter()}\nArea: {self.get_area()}"


    def get_perimeter(self) -> float:
        return 2 * (self.first_side + self.second_side)

    def get_area(self) -> float:
        return self.first_side * self.second_side
