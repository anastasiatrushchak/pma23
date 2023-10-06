from abc import ABC, abstractmethod
from dairy_product_class import DairyProduct
from meat_product_class import MeatProduct

class Factory(ABC):
    @abstractmethod
    def getDairy(self) -> DairyProduct:
        pass

    @abstractmethod
    def getMeat(self) -> MeatProduct:
        pass



