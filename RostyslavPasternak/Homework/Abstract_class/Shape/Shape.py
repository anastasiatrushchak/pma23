from abc import ABC, abstractmethod
from RostyslavPasternak.Homework.Abstract_class.Color import Color
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color
    @abstractmethod
    def get_perimeter(self) -> float:
        pass
    @abstractmethod
    def get_area(self) -> float:
        pass

