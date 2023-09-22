class Color:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return self.color

class Red(Color):
    def __init__(self):
        super.__init__("red")
    def __str__(self):
        return super().__str__()
class Green(Color):
    def __init__(self):
        super.__init__("green")
    def __str__(self):
        return super().__str__()
class Blue(Color):
    def __init__(self):
        super.__init__("blue")
    def __str__(self):
        return super().__str__()
class Yellow(Color):
    def __init__(self):
        super.__init__("yellow")
    def __str__(self):
        return super().__str__()

red = Red

print(red)