from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass

    def __str__(self):
        return self.apply_color()

class RedColor(Color):
    def apply_color(self):
        return "Red"

class BlueColor(Color):
    def apply_color(self):
        return "Blue"

class GreenColor(Color):
    def apply_color(self):
        return "Green"
