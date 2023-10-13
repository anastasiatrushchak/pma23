from abc import ABC, abstractmethod

class Animal():
    def animal_life(self):
        self.name()
        self.get_lapy()
        self.colour()

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def get_lapy(self):
        pass

    @abstractmethod
    def colour(self):
        pass


class Dog(Animal):
    def name(self):
        print("Wow, it is a dog!")

    def get_lapy(self):
        print("It has four legs.")

    def colour(self):
        print("The dog is black.")


class Kangaroo(Animal):
    def name(self):
        print("Wow, it is a kangaroo!")

    def get_lapy(self):
        print("It has two legs.")

    def colour(self):
        print("The kangaroo is orange.")


animal1 = Dog()
animal1.animal_life()
print(" " * 10)
animal2 = Kangaroo()
animal2.animal_life()
