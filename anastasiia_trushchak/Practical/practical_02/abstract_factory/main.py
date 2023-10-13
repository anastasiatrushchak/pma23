from abc import ABC, abstractmethod



class Beverage(ABC):
    def __init__(self, name):
        self.name = name

    def display(self):
        pass


class Hot(Beverage):
    def display(self):
        print(f"{self.name} is hot")


class Ice(Beverage):
    def display(self):
        print(f"{self.name} is ice")


class BeverageFactory(ABC):

    def create(self, name):
        pass


class HotFactory(BeverageFactory):
    def create(self, name):
        return Hot(name)


class IceFactory(BeverageFactory):
    def create(self, name):
        return Ice(name)


hot_factory = HotFactory()
hot_beverage = hot_factory.create("Американо")
hot_beverage.display()

ice_factory = IceFactory()
ice_beverage = ice_factory.create("Сочок")
ice_beverage.display()