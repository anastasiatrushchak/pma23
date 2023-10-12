from factory_class import Factory
from dairy_product_class import DairyProduct
from meat_product_class import MeatProduct
from red_fish_class import RedFish
from coconut_milk_class import CoconutMilk

class EliteFactory(Factory):
    def getDairy(self) -> DairyProduct:
        return CoconutMilk()

    def getMeat(self) -> MeatProduct:
        return RedFish()
