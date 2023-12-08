from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def level_car(self):
        pass

    @abstractmethod
    def type_car(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class BMW(Car):
    def __init__(self, probig):
        self.probig = probig

    def level_car(self):
        return self.probig

    def type_car(self):
        return "sport"

    def __str__(self):
        return "BMW"


class Ferrari(Car):
    def __init__(self, year, probiger):
        self.year = year
        self.probiger = probiger

    def level_car(self):
        return self.year + self.probiger

    def type_area(self):
        return "vintage"

    def __str__(self):
        return "Ferrari"




    def __str__(self):
        return "Square"


class Color(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_color(self):
        return self.color

    @abstractmethod
    def color_set(self, color):
        self.color = color


class Red(Color):
    def __init__(self):
        super().__init__('Red')

    def get_color(self):
        return super().get_color()

    def color_set(self, color):
        return super().set_color()


class Blue(Color):
    def __init__(self):
        super().__init__('Blue')

    def get_color(self):
        return super().get_color()

    def color_set(self, color):
        return super().set_color()


class Yellow(Color):
    def __init__(self):
        super().__init__('Yellow')

    def get_color(self):
        return super().get_color()

    def color_set(self, color):
        return super().set_color()


class Bridge:
    def __init__(self, car, color):
        self.car = car
        self.color = color

    def info(self):
        return (f"{self.color.get_color()} {self.car}"
                f" [Level = {self.car.level_car()} Type = {self.car.type_car()}]")


bm = BMW(5)
bl = Blue()
red_bmw = Bridge(bm, bl)




print(red_bmw.info())


