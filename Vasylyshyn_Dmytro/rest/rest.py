from flask import Flask, jsonify, request
from mongoengine import connect, Document, StringField, IntField, ListField, FloatField
import json

from bson import ObjectId
app = Flask(__name__)

connect("film", host="mongodb://localhost:27017/film")

class Data(Document):
    title = StringField(required=True)
    director = StringField()
    release_year = IntField()
    genre = ListField(StringField())
    cast = ListField(StringField())
    rating = FloatField()
    awards = ListField(StringField())
    plot_summary = StringField()

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        all_data = Data.objects()
        data_list = [
            {
                "id": str(item.id),
                "title": item.title,
                "director": item.director if hasattr(item, 'director') else None,
                "release_year": item.release_year,
                "genre": item.genre,
                "cast": item.cast,
                "rating": item.rating,
                "awards": item.awards,
                "plot_summary": item.plot_summary
            }
            for item in all_data
        ]

        formatted_data = json.dumps(data_list, indent=2, ensure_ascii=False)

        return formatted_data, 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['POST'])
def create_data():
    try:
        if request.is_json:
            new_data = request.json

            data = Data(**new_data)
            data.save()
            return jsonify({"message": "Data created successfully"}), 201
        else:
            return jsonify({"error": "Invalid JSON"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500




@app.route('/api/data/<data_id>', methods=['PATCH'])
def update_data(data_id):
    try:
        if request.is_json:
            updated_data = request.json
            existing_data = Data.objects(id=ObjectId(data_id)).first()

            if existing_data:
                for key, value in updated_data.items():
                    setattr(existing_data, key, value)

                existing_data.save()

                return jsonify({"message": "Data updated successfully"}), 200
            else:
                return jsonify({"error": "Data not found"}), 404
        else:
            return jsonify({"error": "Invalid JSON"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/api/data/<data_id>', methods=['DELETE'])
def delete_data(data_id):
    try:
        data = Data.objects(id=data_id).first()

        if data:
            data.delete()
            return jsonify({"message": "Data deleted successfully"}), 200
        else:
            return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


app.run(debug=True)