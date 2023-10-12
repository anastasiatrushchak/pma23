from abc import ABC, abstractmethod
class Color(ABC):
    @abstractmethod
    def fill_color(self):
        pass

class Red(Color):
    def fill_color(self):
        return "Червоний"

class Green(Color):
    def fill_color(self):
        return "Зелений"

class Blue(Color):
    def fill_color(self):
        return "Синій"