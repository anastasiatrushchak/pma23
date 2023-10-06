from pyxtension.streams import stream
class Passenger:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


passengers = [
    Passenger("Andriy", 26),
    Passenger("Olena", 30),
    Passenger("Ivan", 18),
    Passenger("Maria", 40),
    Passenger("Oleg", 22)
]
older_than_25 = ((stream(passengers)
                 .filter(lambda passenger: passenger.get_age() > 25))
                 .map(lambda passenger: passenger.get_name())
                 .toList())
print("Passengers older than 25 years old:", older_than_25)