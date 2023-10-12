class Color:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

class Red(Color):
    def __init__(self):
        super().__init__("red")

class Green(Color):
    def __init__(self):
        super().__init__("green")

class Blue(Color):
    def __init__(self):
        super().__init__("blue")

class Yellow(Color):
    def __init__(self):
        super().__init__("yellow")

