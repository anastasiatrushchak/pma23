from abc import ABC, abstractmethod

class AbstractDoor(ABC):
    @abstractmethod
    def do_this_door(self):
        pass


class AbstractWindow(ABC):
    @abstractmethod
    def do_this_window(self):
        pass


class AbstractFactory(ABC):
    @abstractmethod
    def create_first_product(self):
        pass

    @abstractmethod
    def create_second_products(self):
        pass
