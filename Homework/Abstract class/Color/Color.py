from enum import Enum
class Color(Enum):
    Red = "red"
    Green = "green"
    Yellow = "yellow"
    Blue = "blue"

class RGB:
    def __init__(self, r,b,g):
        self.red = r
        self.blue = b
        self.green = g