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
def Boys(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()


    result_a = product_a.forboys()
    result_b = product_b.forboys()


    return result_a + "\n" + result_b



def Girls(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()


    result_a = product_a.forgirls()
    result_b = product_b.forgirls()


    return result_a + "\n" + result_b

factory1 = ConcreteToyBoys()
print('For Boys:')
print(Boys(factory1))
print()
factory2 = ConcreteToyGirls()
print('For Girls:')
print(Girls(factory2))