from flask import Flask, jsonify, request
import json

app = Flask(__name__)
file_path = "car_data.json"

class Car:
    def __init__(self, car_id, brand, type, year):
        self.car_id = car_id
        self.brand = brand
        self.type = type
        self.year = year

    def to_dict(self):
        return {
            "id": self.car_id,
            "brand": self.brand,
            "type": self.type,
            "year": self.year
        }

def read_data():
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            cars = [Car(car["id"], car["brand"], car["type"], car["year"]) for car in data]
        return cars
    except FileNotFoundError:
        return []

def write_data(cars):
    data = [car.to_dict() for car in cars]
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

@app.route('/cars', methods=['GET'])
def get_cars():
    cars = read_data()
    return jsonify([car.to_dict() for car in cars])

@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    cars = read_data()
    car = next((c for c in cars if c.car_id == car_id), None)
    if car:
        return jsonify(car.to_dict())
    return jsonify({"message": "Car not found"}), 404

@app.route('/cars', methods=['POST'])
def add_cars():
    new_cars_data = request.json
    existing_cars = read_data()
    new_cars = []
    max_id = max([car.car_id for car in existing_cars]) if existing_cars else 0
    for car_data in new_cars_data:
        max_id += 1
        new_car = Car(max_id, car_data.get('brand'), car_data.get('type'), car_data.get('year'))
        new_cars.append(new_car)

    existing_cars.extend(new_cars)
    write_data(existing_cars)

    return jsonify([car.to_dict() for car in new_cars]), 201

@app.route('/cars/<int:car_id>', methods=['PATCH'])
def update_car(car_id):
    cars = read_data()
    car = next((c for c in cars if c.car_id == car_id), None)
    if car:
        data = request.json
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    if item['id'] == car_id:
                        car.brand = item.get('brand', car.brand)
                        car.type = item.get('type', car.type)
                        car.year = item.get('year', car.year)
                        write_data(cars)
                        return jsonify(car.to_dict())
            return jsonify({"message": "Car not found in the provided list."}), 404
        else:
            return jsonify({"message": "Invalid data format. Expecting a list of objects."}), 400
    return jsonify({"message": "Car not found"}), 404
@app.route('/cars', methods=['PATCH'])
def update_cars_list():
    cars = read_data()
    data = request.json
    if isinstance(data, list):
        for car in cars:
            for item in data:
                if isinstance(item, dict) and item['id'] == car.car_id:
                    car.brand = item.get('brand', car.brand)
                    car.type = item.get('type', car.type)
                    car.year = item.get('year', car.year)
        write_data(cars)
        return jsonify([car.to_dict() for car in cars])
    else:
        return jsonify({"message": "Invalid data format. Expecting a list of objects."}), 400

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    cars = read_data()
    cars = [c for c in cars if c.car_id != car_id]
    write_data(cars)
    return jsonify({"message": "Car deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
