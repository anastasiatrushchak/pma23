from abc import ABC
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
    def move(self):
        pass
    def sleep(self):
        print(f"{self.name} sleep")
    def interact(self):
        self.speak()
        self.move()
        self.sleep()
class Dog(Animal):
    def speak(self):
        print(f"{self.name} gav-gav")
    def move(self):
        print(f"{self.name} run")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} mur-mur")
    def move(self):
        print(f"{self.name} go")

class Bird(Animal):
    def speak(self):
        print(f"{self.name} tsvir-tsvir")
    def move(self):
        print(f"{self.name} fly")


dog = Dog("Baddi")
cat = Cat("Murchuk")
bird = Bird("Kesha")

dog.interact()
cat.interact()
bird.interact()