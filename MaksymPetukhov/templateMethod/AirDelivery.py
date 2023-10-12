from abc import ABC, abstractmethod


class AirDelivery(ABC):
    @abstractmethod
    def load_cargo(self):
        pass

    def deliver_cargo(self):
        print("Delivering postal by air...")

    @abstractmethod
    def unload_cargo(self):
        pass


class PlaneAirDelivery(AirDelivery):
    def load_cargo(self):
        print("Loading cargo to the plane...")

    def unload_cargo(self):
        print("Unloading cargo from the plane...")


class HelicopterAirDelivery(AirDelivery):
    def load_cargo(self):
        print("Loading cargo to the heli...")

    def unload_cargo(self):
        print("Unloading cargo from the plane...")
