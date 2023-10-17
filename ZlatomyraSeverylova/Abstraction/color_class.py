from abc import ABC, abstractmethod

class Color(ABC):

    @abstractmethod
    def color_figure(self):
        pass


class RedColor(Color):
    def __init__(self):
        self.color_figure()
    def color_figure(self):
        self.color = 'Red'


class PurpleColor(Color):
    def __init__(self):
        self.color_figure()
    def color_figure(self):
        self.color = 'Purple'


class PinkColor(Color):
    def __init__(self):
        self.color_figure()
    def color_figure(self):
        self.color = 'Pink'


