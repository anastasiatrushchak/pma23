from abc import ABC, abstractmethod
from Color import Color
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass