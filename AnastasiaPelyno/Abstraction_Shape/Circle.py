from Figure import Figure
from math import pi
class Circle(Figure):
    def __init__(self, colour, radius):
        Figure.__init__(self, colour)
        self.radius=0
        try:
            if radius > 0:
                self.radius = radius
            else:
                raise ValueError
        except ValueError:
            print(f"Помилка:Радіус має бути додатнім числом")
    def area(self):
        if self.radius>0:
            return pi*self.radius**2
        else:
            return None
    def perimetr(self):
        return 2*pi*self.radius
    def __str__(self):
        if self.radius>0:
            return f"Коло: {self.colour.set_colour()}, Площа = {self.area()}, Периметр = {self.perimetr()}"
        else:
            return ""


