from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

lessons_data = []

parser = reqparse.RequestParser()
parser.add_argument("lesson_id")
parser.add_argument('subject')
parser.add_argument('duration')

class LessonList(Resource):
    def get(self):
        return lessons_data

    def post(self):
        args = parser.parse_args()
        lesson_id = args['lesson_id']
        subject = args['subject']
        duration = args['duration']

        if subject is None or duration is None or lesson_id is None:
            return {'message': 'Missing data. Both subject and duration and lesson_id are required.'}, 400

        lesson = {'lesson_id': lesson_id, 'subject': subject, 'duration': duration}
        lessons_data.append(lesson)


        with open('lessons_data.json', 'w') as file:
            json.dump(lessons_data, file, indent=2)

            return {'message': "Lesson added."}, 201

class Lesson(Resource):
    def get(self, lesson_id):
        lesson = next((item for item in lessons_data if item["lesson_id"] == lesson_id), None)
        if lesson:
            return lesson
        return {'message': 'Lesson not found'}, 404

    def patch(self, lesson_id):
        lesson = next((item for item in lessons_data if item["lesson_id"] == lesson_id), None)
        if lesson:
            update_data = request.json
            lesson.update(update_data)
            return {"message": "Lesson updated."}
        return {'message': 'Lesson not found'}, 404

    def delete(self, lesson_id):
        print("Before deletion:", lessons_data)
        lesson = next((item for item in lessons_data if item["lesson_id"] == lesson_id), None)
        if lesson:
            lessons_data.remove(lesson)
   
            with open('lessons_data.json', 'w') as file:
                json.dump(lessons_data, file, indent=2)
            print("After deletion:", lessons_data)
            return {'message': 'Lesson deleted'}
        print("Lesson not found:", lessons_data)
        return {'message': 'Lesson not found'}, 404

api.add_resource(LessonList, '/lessons')
api.add_resource(Lesson, '/lessons/<int:lesson_id>')

if __name__ == "__main__":
    app.run(
        debug=True,
        port=8081
    )
