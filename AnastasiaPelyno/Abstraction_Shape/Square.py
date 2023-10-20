from Rectangle import Rectangle
class Square(Rectangle):
    def __init__(self,colour,side):
        if side>0:
            Rectangle.__init__(self, colour, side, side)
            self.side=side
        else:
            self.side=0
            print(f"Помилка:Сторона квадрата повинна бути додатнім числом")
    def __str__(self):
        if self.side>0:
            return f"Квадрат:{self.colour.set_colour()} , Площа = {self.area()}, Периметр = {self.perimetr()}"
        else:
            return ""