from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass


class RedColor(Color):
    def apply_color(self):
        return "Red"


class GreenColor(Color):
    def apply_color(self):
        return "Green"


class BlueColor(Color):
    def apply_color(self):
        return "Blue"
