from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pymongo
from bson import json_util
import constants

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('brand')
parser.add_argument('model')

client = pymongo.MongoClient(constants.DB_URL)
db = client["test"]
collection = db["cars"]

class CarList(Resource):
    def get(self):
        cars = list(collection.find({}, {'_id': 0}))
        return cars

    def post(self):
        brand = request.json.get('brand')
        model = request.json.get('model')

        if brand is None or model is None:
            return {'message': 'Missing data. Both brand and model are required.'}, 400

        car = {'brand': brand, 'model': model}
        collection.insert_one(car)
        return {'message': "Car added."}, 201

class Car(Resource):
    def get(self, car_id):
        car = collection.find_one({"id": car_id}, {'_id': 0})
        if car:
            return json_util.dumps(car)
        return {'message': 'Car not found'}, 404

    def patch(self, car_id):
        car = collection.find_one({"id": car_id})
        if car:
            update_data = request.json
            collection.update_one({"id": car_id}, {"$set": update_data})
            return {"message": "Car updated."}
        return {'message': 'Car not found'}, 404

    def delete(self, car_id):
        car = collection.find_one({"id": car_id})
        if car:
            collection.delete_one({"id": car_id})
            return {'message': 'Car deleted'}
        return {'message': 'Car not found'}, 404

api.add_resource(CarList, '/cars')
api.add_resource(Car, '/cars/<int:car_id>')

if __name__ == "__main__":
    app.run(debug=True)
