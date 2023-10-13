from shape import Shape
from abc import ABC, abstractmethod


class Colour(ABC):
    @abstractmethod
    def paint_shape(self):
        pass


