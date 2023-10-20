from Abstract import AbstractDoor, AbstractFactory, AbstractWindow


class ConcreteOak(AbstractDoor):
    def do_this_door(self):
        return "We make oak doors."


class ConcreteSpruce(AbstractDoor):
    def do_this_door(self):
        return "We make spruce door."


class ConcreteWooden(AbstractWindow):
    def do_this_window(self):
        return "We make wooden windows"


class ConcretePlastic(AbstractWindow):
    def do_this_window(self):
        return "We make plastic windows"


class ConcreteSmereka(AbstractFactory):
    def create_first_product(self):
        return ConcreteOak()

    def create_second_products(self):
        return ConcreteWooden()


class ConcreteSteko(AbstractFactory):
    def create_first_product(self):
        return ConcreteSpruce()

    def create_second_products(self):
        return ConcretePlastic()
