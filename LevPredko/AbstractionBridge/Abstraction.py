from abc import ABC, abstractmethod


class Color(ABC):
    def shape_color(self):
        pass


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def shape_method(self):
        pass

    @abstractmethod
    def shape_perimeter(self):
        pass

    @abstractmethod
    def shape_area(self):
        pass
