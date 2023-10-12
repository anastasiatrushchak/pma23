from factory_class import Factory
from dairy_product_class import DairyProduct
from meat_product_class import MeatProduct
from milk_class import Milk
from pork_class import Pork

class CommonFactory(Factory):
    def getDairy(self) -> DairyProduct:
        return Milk()

    def getMeat(self) -> MeatProduct:
        return Pork()
