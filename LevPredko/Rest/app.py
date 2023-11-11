from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from bson import json_util
import pymongo

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('brand')
parser.add_argument('model')

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["university_levpredko"]
collection = db["phones"]

class PhoneList(Resource):
    def get(self):
        phones = list(collection.find({}, {'_id': 0}))
        return phones

    def post(self):
        id = request.json.get('id')
        brand = request.json.get('brand')
        model = request.json.get('model')

        if brand is None or model is None or id is None:
            return {'message': 'Missing data. Both brand and model and id are required.'}, 400

        phone = {'id': id,'brand': brand, 'model': model}
        collection.insert_one(phone)
        return {'id :''message': "Phone added."}, 201


class Phone(Resource):
    def get(self, phone_id):
        phone = collection.find_one({"id": phone_id}, {'_id': 0})
        if phone:
            return json_util.dumps(phone)
        return {'message': 'Phone not found'}, 404

    def patch(self, phone_id):
        phone = collection.find_one({"id": phone_id})
        if phone:
            update_data = request.json
            collection.update_one({"id": phone_id}, {"$set": update_data})
            return {"message": "Phone updated."}
        return {'message': 'Phone not found'}, 404

    def delete(self, phone_id):
        phone = collection.find_one({"id": phone_id})
        if phone:
            collection.delete_one({"id": phone_id})
            return {'message': 'Phone deleted'}
        return {'message': 'Phone not found'}, 404

api.add_resource(PhoneList, '/phone')
api.add_resource(Phone, '/phone/<int:phone_id>')

app.run(debug=True)