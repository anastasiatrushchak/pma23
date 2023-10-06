from abc import ABC, abstractmethod


class Transport(ABC):
    def run(self):
        self.transportType()
        self.prepareTransport()
        self.startEngine()
        self.travel()

    @abstractmethod
    def transportType(self):
        pass

    @abstractmethod
    def prepareTransport(self):
        pass

    def startEngine(self):
        print("Starting engine!")

    @abstractmethod
    def travel(self):
        pass


class Ship(Transport):
    def transportType(self):
        print("Ship")

    def prepareTransport(self):
        print("Cleaning board, filling tank")

    def travel(self):
        print("Traveling by sea...")


class Car(Transport):

    def transportType(self):
        print("Car")

    def prepareTransport(self):
        print("Adjust the mirrors, inflate the tires")

    def travel(self):
        print("Traveling by ground...")

class Plane(Transport):

    def transportType(self):
        print("Plane")

    def prepareTransport(self):
        print("Checking the flaps, charging APU")

    def travel(self):
        print("Traveling by air...")

vehicle1 = Ship()
vehicle1.run()
print()
vehicle2 = Car()
vehicle2.run()
print()
vehicle3 = Plane()
vehicle3.run()
