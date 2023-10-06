from abc import ABC


class Product(ABC):
    def __init__(self, name):
        self.name = name

    def display(self):
        pass


class Food(Product):
    def display(self):
        print(f"{self.name} is food")


class Drink(Product):
    def display(self):
        print(f"{self.name} is drink")


class ProductFactory(ABC):

    def create(self, name):
        pass



class FoodFactory(ProductFactory):
    def create(self, name):
        return Food(name)



class DrinkFactory(ProductFactory):
    def create(self, name):
        return Drink(name)



food_factory = FoodFactory()
food_product = food_factory.create("Pizza")
food_product.display()

drink_factory = DrinkFactory()
drink_product = drink_factory.create("Juice")
drink_product.display()
