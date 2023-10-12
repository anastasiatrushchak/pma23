from abc import ABC, abstractmethod

class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

class FastCarFactory(CarFactory):
    def create_car(self):
        return FastCar()

class SlowCarFactory(CarFactory):
    def create_car(self):
        return SlowCar()

class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def template_method(self):
        self.start()
        self.drive()
        self.stop()

class FastCar(Car):
    def start(self):
        print("Старт швидкісного автомобіля")

    def drive(self):
        print("Швидкісний автомобіль рухається швидко")

    def stop(self):
        print("Зупинка швидкісного автомобіля")

class SlowCar(Car):
    def start(self):
        print("Старт повільного автомобіля")

    def drive(self):
        print("Повільний автомобіль рухається повільно")

    def stop(self):
        print("Зупинка повільного автомобіля")

class CarUser:
    def __init__(self, factory):
        self.factory = factory

    def use_car(self):
        car = self.factory.create_car()
        print("Автомобіль:")
        car.template_method()

fast_car_factory = FastCarFactory()
slow_car_factory = SlowCarFactory()

car_user_1 = CarUser(fast_car_factory)
car_user_2 = CarUser(slow_car_factory)

car_user_1.use_car()
car_user_2.use_car()
