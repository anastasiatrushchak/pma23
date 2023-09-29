from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

class Sedan(Transport):
    def start(self):
        return "Sedan is starting."

    def stop(self):
        return "Sedan is stopping."

class SportMotorcycle(Transport):
    def start(self):
        return "Sport Motorcycle is starting."

    def stop(self):
        return "Sport Motorcycle is stopping."


class SedanFactory(VehicleFactory):
    def create_car(self):
        return Sedan()


class SportMotorcycleFactory(VehicleFactory):
    def create_car(self):
        return SportMotorcycle()



sedan_factory = SedanFactory()
sedan = sedan_factory.create_car()
print(sedan.start())

motorcycle_factory = SportMotorcycleFactory()
motorcycle = motorcycle_factory.create_car()
print(motorcycle.start())
