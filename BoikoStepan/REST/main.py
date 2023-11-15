from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    videos = db.Column(db.Integer)

with app.app_context():
    db.create_all()


parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("videos")

class Main(Resource):
    def get(self, course_id):
        course = Course.query.get(course_id)
        if course:
            return {'id': course.id, 'name': course.name, 'videos': course.videos}
        return {'message': 'course not found'}, 404

    def patch(self, course_id):
        args = parser.parse_args()
        course = Course.query.get(course_id)
        if course:
            if args['name']:
                course.name = args['name']
            if args['videos']:
                course.videos = args['videos']
            db.session.commit()
            return {'id': course.id, 'name': course.name, 'videos': course.videos}
        return {'message': 'course not found'}, 404

    def delete(self, course_id):
        course = Course.query.get(course_id)
        if course:
            db.session.delete(course)
            db.session.commit()
            return {'message': 'course deleted'}
        return {'message': 'course not found'}, 404

class Video(Resource):
    def get(self):
        courses = Course.query.all()
        return [{'id': course.id, 'name': course.name, 'videos': course.videos} for course in courses]

    def post(self):
        args = parser.parse_args()
        course = Course(name=args['name'], videos=args['videos'])
        db.session.add(course)
        db.session.commit()
        return {'id': course.id, 'name': course.name, 'videos': course.videos}

api.add_resource(Video, "/courses")
api.add_resource(Main, "/courses/<int:course_id>")

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
