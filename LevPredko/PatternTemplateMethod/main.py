from abc import ABC, abstractmethod


class Template(ABC):
    def template_method(self):
        self.step1()
        self.step2()
        self.step3()


    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass

class ConcreteClass(Template):
    def step1(self):
        print("Виконуємо крок 1")

    def step2(self):
        print("Виконуємо крок 2")

    def step3(self):
        print("Виконуємо крок 3")

template = ConcreteClass()
template.template_method()
