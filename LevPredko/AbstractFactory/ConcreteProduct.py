from Abstract import AbstractCar, AbstractFactory, AbstractGlassProducts

class ConcreteCar(AbstractCar):
    def do_something(self):
        return "We make cars."


class ConcreteAirСonditioning(AbstractCar):
    def do_something(self):
        return "We make air conditioning."


class ConcreteWindows(AbstractGlassProducts):
    def do_another_thing(self):
        return "We make windows"


class ConcreteShowcase(AbstractGlassProducts):
    def do_another_thing(self):
        return "We make showcase"


class ConcreteMitsubishi(AbstractFactory):
    def create_product_a(self):
        return ConcreteCar()

    def create_product_b(self):
        return ConcreteWindows()

class ConcreteSteko(AbstractFactory):
    def create_product_a(self):
        return ConcreteAirСonditioning()

    def create_product_b(self):
        return ConcreteShowcase()
