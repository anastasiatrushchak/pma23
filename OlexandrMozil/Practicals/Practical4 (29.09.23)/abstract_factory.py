from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def create_phone(self, model):
        pass

    @abstractmethod
    def create_computer(self, model):
        pass


class SamsungPhone:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return self.model


class DellComputer:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return self.model


class SamsungFactory(Factory):
    def create_phone(self, model):
        return SamsungPhone(model)

    def create_computer(self, model):
        return DellComputer(model)


class DellFactory(Factory):
    def create_phone(self, model):
        return SamsungPhone(model)

    def create_computer(self, model):
        return DellComputer(model)


samsung_factory = SamsungFactory()
samsung_phone = samsung_factory.create_phone("Samsung Phone")
samsung_computer = samsung_factory.create_computer("Samsung Computer")

dell_factory = DellFactory()
dell_phone = dell_factory.create_phone("Dell Phone")
dell_computer = dell_factory.create_computer("Dell Computer")

print(f"Samsung Factory: {samsung_phone} and {samsung_computer}")
print(f"Dell Factory: {dell_phone} and {dell_computer}")
