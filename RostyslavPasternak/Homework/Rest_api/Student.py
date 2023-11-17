from flask_restful import Resource, Api, reqparse
from flask import Flask, request
import mongo

class Student(Resource):
    def get(self, student_id):
        student = mongo.collection.find_one({"student_id": student_id}, {'_id': 0})
        if student:
            return student
        return {'message': 'student not found'}, 404

    def patch(self, student_id):
        student = mongo.collection.find_one({"student_id": student_id})
        if student:
            update_data = request.json
            mongo.collection.update_one({"student_id": student_id}, {"$set": update_data})
            return {"message": "Student updated."}
        return {'message': 'Student not found'}, 404

    def delete(self, student_id):
        student = mongo.collection.find_one({"student_id": student_id})
        if student:
            mongo.collection.delete_one({"student_id": student_id})
            return {'message': 'Student deleted'}
        return {'message': 'Student not found'}, 404
