from flask import Flask, jsonify, request, make_response
from flask_pymongo import PyMongo
import pymongo
import json
from bson import json_util
from bson.objectid import ObjectId


def parse_json(data):
    return json.loads(json_util.dumps(data))


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/product"
mongo = PyMongo(app)


@app.route('/products', methods=['GET'])
def get_products():
    myproduct = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myproduct["Product"]
    mycol = mydb["products"]
    return parse_json(list(mycol.find()))


@app.route('/products', methods=['POST'])
def create_product():
    name = request.json['name']
    date = request.json['date']
    carbohydrates = request.json['carbohydrates']
    proteins = request.json['proteins']
    fats = request.json['fats']
    calories = request.json['calories']

    if name and date and carbohydrates and proteins and fats and calories:
        myproduct = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myproduct["Product"]
        mycol = mydb["products"]

        mydict = {'name': name, 'date': date, 'carbohydrates': carbohydrates,
                  'proteins': proteins, 'fats': fats, 'calories': calories}

        x = mycol.insert_one(mydict)

        response = jsonify({
            '_id': str(x.inserted_id),
            'name': name,
            'date': date,
            'carbohydrates': carbohydrates,
            'proteins': proteins,
            'fats': fats,
            'calories': calories
        })
        response.status_code = 201
        return response
    else:
        return make_response(jsonify({"message": "not given all data"}), 404)


@app.route('/products/<product_id>', methods=['PATCH'])
def update_product(product_id):
    name = request.json['name']
    date = request.json['date']
    carbohydrates = request.json['carbohydrates']
    proteins = request.json['proteins']
    fats = request.json['fats']
    calories = request.json['calories']
    print(product_id)
    if name and date and carbohydrates and proteins and fats and calories and product_id:
        myproduct = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myproduct["Product"]
        mycol = mydb["products"]

        x = mycol.update_one(filter={"_id": ObjectId(product_id)},
                             update={"$set": {'name': name, 'date': date, 'carbohydrates': carbohydrates,
                                              'proteins': proteins, 'fats': fats, 'calories': calories}})

        response = jsonify({
            '_id': str(product_id),
            'name': name,
            'date': date,
            'carbohydrates': carbohydrates,
            'proteins': proteins,
            'fats': fats,
            'calories': calories
        })
        response.status_code = 201
        return response
    else:
        return make_response(jsonify({"message": "not given all data"}), 404)


@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id:
        myproduct = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myproduct["Product"]
        mycol = mydb["products"]

        x = mycol.delete_one(filter={"_id": ObjectId(product_id)})


        if x.deleted_count>0:
            return make_response(jsonify({"message": "product is deleted"}), 200)
        else:
            return make_response(jsonify({"message": "product is not deleted"}), 400)
    else:
        return make_response(jsonify({"message": "not given all data"}), 404)

if __name__ == '__main__':
    app.run(debug=True)

# import pymongo
#
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["Product"]
# mycol = mydb["products"]
#
# for x in mycol.find():
#   print(x)
#
# mydict = { 'name': 'SMTH', 'date': '2023-02-15', 'carbohydrates': 27, 'proteins': 1, 'fats': 0.3, 'calories': 95 }
#
# x = mycol.insert_one(mydict)
# print(x)
