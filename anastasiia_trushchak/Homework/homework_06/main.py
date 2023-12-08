def print_cars(cars):
    for car, characteristics in cars.items():
        print(f"Car: {car}")
        print(f"Year: {characteristics['year']}")
        print(f"Color: {characteristics['color']}")
        print(f"Type: {characteristics['type']}")
        print()

cars = {
    'BMW': {
        'year': 2023,
        'color': 'black',
        'type': 'sport'
    },
    'Mercedes': {
        'year': 1980,
        'color': 'red',
        'type': 'supercar'
    },
    'Rangerover': {
        'year': 2018,
        'color': 'yellow',
        'type': 'SUV'
    }
}

print_cars(cars)

try:
    cars.pop('Mercedes')
    print("Dictionary after removing the mercedes")
except KeyError:
    print("Car not found in the dictionary")

print_cars(cars)

try:
    cars['BMW']['color'] = 'brown'
    cars['Rangerover']['year'] = 2020
    print("Dictionary after changing the color of the BMW and the year of the Rangerover")
except KeyError:
    print("Car or characteristics not found in the dictionary")

print_cars(cars)

cars['Tesla'] = {
    'year': 2022,
    'color': 'white',
    'type': 'electric'
}

print("Dictionary after adding a Tesla")
print_cars(cars)
