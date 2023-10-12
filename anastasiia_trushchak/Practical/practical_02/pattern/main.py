from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    def interact(self):
        self.move()
        self.make_sound()


class Car(Transport):
    def move(self):
        print(f"{self.name} is driving")

    def make_sound(self):
        print(f"{self.name} honks")


class Bicycle(Transport):
    def move(self):
        print(f"{self.name} is pedaling")

    def make_sound(self):
        print(f"{self.name} rings the bell")


class Plane(Transport):
    def move(self):
        print(f"{self.name} is flying")

    def make_sound(self):
        print(f"{self.name} makes engine noise")


car = Car("Toyota")
bicycle = Bicycle("BMX")
plane = Plane("Boeing 747")

car.interact()
bicycle.interact()
plane.interact()
