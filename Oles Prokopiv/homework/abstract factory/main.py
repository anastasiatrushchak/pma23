from concrete import AppleTechDeviceFactory, SamsungTechDeviceFactory

def order_technology(factory):
    smartphone = factory.create_smartphone()
    tablet = factory.create_tablet()
    laptop = factory.create_laptop()

    print("Замовлено:")
    print(smartphone.info())
    print(tablet.info())
    print(laptop.info())

apple_factory = AppleTechDeviceFactory()
order_technology(apple_factory)

samsung_factory = SamsungTechDeviceFactory()
order_technology(samsung_factory)
