from abc import ABC, abstractmethod

class Colors(ABC):
    @abstractmethod
    def get_color(self):
        pass


class Black(Colors):
    def get_color(self):
        return "Black"


class Red(Colors):
    def get_color(self):
        return "Red"


class White(Colors):
    def get_color(self):
        return "White"


RED = Red()
BLACK = Black()
WHITE = White()
