from abc import ABC, abstractmethod
#Template Method
class A(ABC):
    def __init__(self):
        print("Constructor A")

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def second(self):
        pass

    def template(self):
        self.first()
        self.second()

class B(A):
    def __init__(self):
        print("b")
        super().__init__()

    def first(self):
        print(1234)

    def second(self):
        print(98765)

b_instance = B()
b_instance.template()