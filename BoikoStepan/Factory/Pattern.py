from abc import ABC, abstractmethod


class MakeMeal(ABC):

    def prepare(self): pass

    def cook(self): pass

    def eat(self): pass

    def go(self):
        self.prepare()
        self.cook()
        self.eat()


class MakePizza(MakeMeal):
    def prepare(self):
        print("Prepare Pizza")

    def cook(self):
        print("Cook Pizza")

    def eat(self):
        print("Eat Pizza")


class MakeCake(MakeMeal):
    def prepare(self):
        print("Prepare Ingredients")

    def cook(self):
        print("Cook Cake")

    def eat(self):
        print("Eat Cake")


makePizza = MakePizza()
makePizza.go()

print(25 * "-")

makeTea = MakeCake()
makeTea.go()