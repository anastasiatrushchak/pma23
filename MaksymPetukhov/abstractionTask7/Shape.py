from abc import ABC, abstractmethod
import Color


class Shape(ABC):

    def __init__(self, color: Color):
        if color is None:
            raise ValueError("Color can not be None")
        else:
            self.color = color

    def __str__(self):
        #with color, perimeter and area
        return f"{self.color.get_color()} {self.__class__.__name__} perimeter = {self.get_perimeter()}, area = {self.get_area()}"
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass
