from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pymongo
from bson import json_util

app = Flask(__name__)
api = Api(app)

DB_URL = "mongodb://localhost:27017/"
parser = reqparse.RequestParser()
parser.add_argument("client_id")
parser.add_argument('name')
parser.add_argument('surname')

client = pymongo.MongoClient(DB_URL)
db = client["clientsdb"]
collection = db["clients"]

class ClientList(Resource):
    def get(self):
        clients = list(collection.find({}, {'_id': 0}))
        return clients

    def post(self):
        client_id = request.json.get('client_id')
        name = request.json.get('name')
        surname = request.json.get('surname')

        if name is None or surname is None or id is None:
            return {'message': 'Missing data. Both name and surname and client_id are required.'}, 400

        client = {'client_id': client_id,'name': name, 'surname': surname}
        collection.insert_one(client)
        return {'message': "Client added."}, 201

class Client(Resource):
    def get(self, client_id):
        client = collection.find_one({"client_id": client_id}, {'_id': 0})
        if client:
            return json_util.dumps(client)
        return {'message': 'Client not found'}, 404

    def patch(self, client_id):
        client = collection.find_one({"client_id": client_id})
        if client:
            update_data = request.json
            collection.update_one({"client_id": client_id}, {"$set": update_data})
            return {"message": "Client updated."}
        return {'message': 'Client not found'}, 404

    def delete(self, client_id):
        client = collection.find_one({"client_id": client_id})
        if client:
            collection.delete_one({"client_id": client_id})
            return {'message': 'Client deleted'}
        return {'message': 'Client not found'}, 404

api.add_resource(ClientList, '/clients')
api.add_resource(Client, '/clients/<int:client_id>')

if __name__ == "__main__":
    app.run(debug=True)
