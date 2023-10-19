from abc import ABC
class Figure(ABC):
    def __init__(self,colour):
        self.colour=colour
    def area(self):
        pass
    def perimetr(self):
        pass
    def __str__(self):
        pass