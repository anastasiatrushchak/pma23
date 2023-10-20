# Основний клас для кольорів
class Color:
    def __init__(self):
        pass

    def fill_color(self):
        pass


# Клас для жовтого кольору, успадковує властивості від Color
class YellowColor(Color):
    def fill_color(self):
        return "жовтий"


# Клас для зеленого кольору, успадковує властивості від Color
class GreenColor(Color):
    def fill_color(self):
        return "зелений"


# Клас для червоного кольору, успадковує властивості від Color
class RedColor(Color):
    def fill_color(self):
        return "червоний"
