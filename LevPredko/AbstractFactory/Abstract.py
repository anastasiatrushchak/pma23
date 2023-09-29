from abc import ABC, abstractmethod

class AbstractCar(ABC):
    @abstractmethod
    def do_something(self):
        pass


class AbstractGlassProducts(ABC):
    @abstractmethod
    def do_another_thing(self):
        pass


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass
