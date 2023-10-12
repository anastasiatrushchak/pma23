from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, colour):
        self.colour = colour

    def paint(self):
        self.colour.paint_shape()

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def area(self):
        pass





