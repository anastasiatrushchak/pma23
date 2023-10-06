import abc

class AbstractProductA(abc.ABC):
    @abc.abstractmethod
    def operation_a(self):
        pass

class AbstractProductB(abc.ABC):
    @abc.abstractmethod
    def operation_b(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        print("Concrete Product A1 operation")

class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        print("Concrete Product B1 operation")

class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        print("Concrete Product A2 operation")

class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        print("Concrete Product B2 operation")

class AbstractFactory(abc.ABC):
    @abc.abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abc.abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

factory1 = ConcreteFactory1()
product_a1 = factory1.create_product_a()
product_b1 = factory1.create_product_b()
product_a1.operation_a()
product_b1.operation_b()

factory2 = ConcreteFactory2()
product_a2 = factory2.create_product_a()
product_b2 = factory2.create_product_b()
product_a2.operation_a()
product_b2.operation_b()
