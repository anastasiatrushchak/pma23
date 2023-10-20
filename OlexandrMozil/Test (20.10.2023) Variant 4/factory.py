from abc import ABC


class Item(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def create_item(self):
        pass


class Wheel(Item):
    def __init__(self, name, price, radius):
        super().__init__(name, price)
        self.radius = radius

    def create_item(self):
        return f"Name: {self.name}, Price: {self.price}, Radius: {self.radius}"


class Engine(Item):
    def __init__(self, name, price, power):
        super().__init__(name, price)
        self.power = power

    def create_item(self):
        return f"Name: {self.name}, Price: {self.price}, Power: {self.power}"


class Factory(ABC):
    def make_item(self, item: Item):
        pass


class WheelFactory(Factory):
    def make_item(self, wheel: Wheel):
        return wheel.create_item()


class EngineFactory(Factory):
    def make_item(self, engine: Engine):
        return engine.create_item()


factory = Factory()
wheel_factory = WheelFactory()
engine_factory = EngineFactory()
wheel = Wheel("SportWheel", 100, 50)
engine = Engine("SportEngine", 1000, 100)
print(wheel_factory.make_item(wheel))
print(engine_factory.make_item(engine))