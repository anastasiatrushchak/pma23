from flask_restful import Resource
from flask import request
import mongo
class StudentList(Resource):
    def get(self):
        students = list(mongo.collection.find({}, {'_id': 0}))
        return students

    def post(self):
        surname = request.json.get('surname')
        grade = request.json.get('grade')

        if surname is None or grade is None:
            return {'message': 'Missing data. Both are surname and grade  required.'}, 400

        student = {'surname': surname, 'grade': grade}
        mongo.collection.insert_one(student)
        return {'message': "student added."}, 201
