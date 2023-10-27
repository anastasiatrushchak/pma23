from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, color ):
        self.color = color

    @abstractmethod
    def calculate_perim(self):
        pass

    @abstractmethod
    def calculate_square(self):
        pass

    def __str__(self):
        return f'Color: {self.color.get_color()}, Square: {self.calculate_square()}, Perimeter: {self.calculate_perim()}'

