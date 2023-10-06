from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class AbstractBoys(ABC):
    @abstractmethod
    def forboys(self):
        pass


class AbstractGirls(ABC):
    @abstractmethod
    def forgirls(self):
        pass
