from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def create_phone(self):
        pass

    @abstractmethod
    def create_computer(self):
        pass


class AbstractPhone(ABC):
    @abstractmethod
    def make_phone(self):
        pass


class AbstractComputer(ABC):
    @abstractmethod
    def make_computer(self):
        pass


class ConcreteIphone(AbstractPhone):
    def make_phone(self):
        return "We made concrete Iphone"


class ConcreteRedmi(AbstractPhone):
    def make_phone(self):
        return "We made concrete Redmi"


class ConcreteMacbook(AbstractComputer):
    def make_computer(self):
        return "We made concrete Macbook"


class ConcreteXiaomiLaptop(AbstractComputer):
    def make_computer(self):
        return "We made concrete Xiaomi Laptop"


class Apple(Factory):
    def create_phone(self):
        return ConcreteIphone()

    def create_computer(self):
        return ConcreteMacbook()


class Xiaomi(Factory):
    def create_phone(self):
        return ConcreteRedmi()

    def create_computer(self):
        return ConcreteXiaomiLaptop()


def create_product(fabric):
    phone = fabric.create_phone()
    computer = fabric.create_computer()

    const_phone = phone.make_phone()
    const_computer = computer.make_computer()

    return const_phone + "\n" + const_computer


print("Apple Factory:")
fabric1 = Apple()
print(create_product(fabric1))
print("\nXiaomi Factory:")
fabric2 = Xiaomi()
print(create_product(fabric2))
