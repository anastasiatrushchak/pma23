from abc import ABC, abstractmethod
from AirDelivery import AirDelivery, PlaneAirDelivery, HelicopterAirDelivery
from GroundDelivery import GroundDelivery, TruckGroundDelivery
class LogisticsFactory(ABC):
    @abstractmethod
    def create_air_delivery_service(self) -> AirDelivery:
        pass

    @abstractmethod
    def create_ground_delivery_service(self) -> GroundDelivery:
        pass

class DeliveringServices(LogisticsFactory):
    def create_air_delivery_service(self) -> AirDelivery:
        return PlaneAirDelivery()

    def create_ground_delivery_service(self) -> GroundDelivery:
        return TruckGroundDelivery()