from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_perimeter(self) -> float:
        pass
    @abstractmethod
    def get_area(self) -> float:
        pass
