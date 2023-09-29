from abc import ABC, abstractmethod


class Recipe(ABC):
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


class Omelet(Recipe):
    def step1(self):
        print("1. Beat the eggs while melting the butter on pan")

    def step2(self):
        print("2. Add the beaten eggs to the pan and fill it with cheese or sausages")

    def step3(self):
        print("3. Fold the omelette in half and serve it on the plate")

    def __init__(self):
        self.template_method()


class Sandwich(Recipe):
    def step1(self):
        print("1. Assemble your sandwich by layering deli meat,"
              " cheese, and any desired veggies between two slices of bread.")

    def step2(self):
        print("2. Add condiments like mayo or mustard if you like")

    def step3(self):
        print("3. Serve and enjoy")




print("Omlet recipe:")
a = Omelet()
a.template_method()

print("\nSandwich recipe:")
b = Sandwich()
b.template_method()