from abc import ABC, abstractmethod


class AnimalFactory(ABC):
    @abstractmethod
    def grow_animal(self):
        pass


class DomesticAnimalFactory(AnimalFactory):
    def grow_animal(self):
        return Cat()


class WildAnimalFactory(AnimalFactory):
    def grow_animal(self):
        return Fox()


class Animal(ABC):
    @abstractmethod
    def output(self):
        pass

class Cat(Animal):
    def output(self):
        print("I am a cat!")


class Fox(Animal):
    def output(self):
        print("I am a fox!")


wild_factory = WildAnimalFactory()
animal = wild_factory.grow_animal()

domestic_factory = DomesticAnimalFactory()
pet = domestic_factory.grow_animal()
animal.output()
pet.output()


