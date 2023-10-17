from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Color(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_color(self):
        return self.color

    @abstractmethod
    def color_set(self, color):
        self.color = color