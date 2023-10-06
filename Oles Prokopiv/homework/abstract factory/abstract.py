from abc import ABC, abstractmethod

class TechDeviceFactory(ABC):
    @abstractmethod
    def create_smartphone(self):
        pass

    @abstractmethod
    def create_tablet(self):
        pass

    @abstractmethod
    def create_laptop(self):
        pass
class TechPhone(ABC):
    @abstractmethod
    def info(self):
        pass

class TechTab(ABC):
    @abstractmethod
    def info(self):
        pass

class TechBook(ABC):
    @abstractmethod
    def info(self):
        pass