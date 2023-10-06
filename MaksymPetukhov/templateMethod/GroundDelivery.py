from abc import ABC, abstractmethod


class GroundDelivery(ABC):
    @abstractmethod
    def load_cargo(self):
        pass

    def deliver_cargo(self):
        print("Delivering postal by roads...")

    @abstractmethod
    def unload_cargo(self):
        pass


class TruckGroundDelivery(GroundDelivery):
    def load_cargo(self):
        print("Loading cargo to the trailer...")

    def unload_cargo(self):
        print("Unloading cargo from the trailer...")
