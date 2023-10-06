from LogisticsFactory import DeliveringServices

factory = DeliveringServices()
air_service = factory.create_air_delivery_service()
ground_service = factory.create_ground_delivery_service()

air_service.load_cargo()
air_service.deliver_cargo()
air_service.unload_cargo()
print()
ground_service.load_cargo()
ground_service.deliver_cargo()
ground_service.unload_cargo()
