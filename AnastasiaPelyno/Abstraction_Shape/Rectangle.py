from Figure import Figure
class Rectangle(Figure):
    def __init__(self,colour,width,height):
        Figure.__init__(self, colour)
        self.width=0
        self.height=0
        try:
            if width>0 and height>0:
                self.width=width
                self.height=height
            else:
                raise ValueError

        except ValueError:
            print(f"Помилка:Сторони прямокутника повинні бути додатніми числами")
    def area(self):
        return self.width*self.height
    def perimetr(self):
        return 2*(self.width+self.height)
    def __str__(self):
        if self.width > 0 and self.height > 0:
             return f"Прямокутник:{self.colour.set_colour()} , Площа = {self.area()}, Периметр = {self.perimetr()}"
        else:
            return ""
