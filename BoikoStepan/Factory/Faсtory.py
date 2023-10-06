from Abstract import AbstractBoys, AbstractFactory, AbstractGirls

class Toy_Car(AbstractBoys):
    def forboys(self):
        return "We make toy cars."


class DesignerLEGO(AbstractBoys):
    def forboys(self):
        return "We make designer LEGO."


class Dolls(AbstractGirls):
    def forgirls(self):
        return "We make dolls"


class ToyDishes(AbstractGirls):
    def forgirls(self):
        return "We make toy dishes"


class ConcreteToyBoys(AbstractFactory):
    def create_product_a(self):
        return Toy_Car()

    def create_product_b(self):
        return DesignerLEGO()

class ConcreteToyGirls(AbstractFactory):
    def create_product_a(self):
        return Dolls()

    def create_product_b(self):
        return ToyDishes()




