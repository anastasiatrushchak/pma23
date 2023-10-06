from abc import ABC, abstractmethod

class Person(ABC):

    def templateMethod(self):
        self.name()
        self.age()
        self.wight()
        self.height()
        self.glasses()

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def wight(self):
        pass

    @abstractmethod
    def height(self):
        pass

    def tatoo(self):
        pass

    def glasses(self):
        pass


