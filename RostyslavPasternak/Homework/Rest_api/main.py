from flask import Flask
from flask_restful import Api, reqparse
from Student import Student
from StudentList import StudentList
DB_URL = "mongodb://localhost:27017/"

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('surname')
parser.add_argument('grade')



api.add_resource(StudentList, '/students')
api.add_resource(Student, '/students/<int:student_id>')

if __name__ == "__main__":
    app.run(debug=True, port=5002)





