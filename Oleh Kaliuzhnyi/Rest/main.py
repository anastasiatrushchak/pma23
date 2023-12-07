from flask import Flask, jsonify, request
from mongoengine import connect, Document, StringField, IntField, FloatField
import json
from bson import ObjectId

app = Flask(__name__)

connect("books", host="mongodb+srv://Oleh:KqT5d7V667JDe9wL@cluster0.grxv3oe.mongodb.net/books.data")


class Book(Document):
    name = StringField(required=True)
    author = StringField()
    cover_type = StringField()
    language = StringField()
    pages_number = IntField()
    publishing_house = StringField()
    release_year = IntField()
    rating = FloatField()


@app.route('/api/data', methods=['GET'])
def get_book():
    try:
        all_data = Book.objects()
        books_list = [
            {
                "id": str(item.id),
                "name": item.name,
                "author": item.author,
                "cover_type": item.cover_type,
                "language": item.language,
                "pages_number": item.pages_number,
                "publishing_house": item.publishing_house,
                "release_year": item.release_year,
                "rating": item.rating
            }
            for item in all_data
        ]

        parsed_books = json.dumps(books_list, indent=2, ensure_ascii=False)

        return parsed_books, 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as err:
        return jsonify({"error": str(err)}), 500


@app.route('/api/data', methods=['POST'])
def create_book():
    try:
        if request.is_json:
            new_book = request.json
            book = Book(**new_book)
            book.save()
            return jsonify({"message": "Data created successfully"}), 201
        else:
            return jsonify({"error": "Invalid JSON"}), 400
    except Exception as err:
        return jsonify({"error": str(err)}), 500


@app.route('/api/data/<book_id>', methods=['PATCH'])
def update_book(book_id):
    try:
        if request.is_json:
            updated_book = request.json
            existing_book = Book.objects(id=ObjectId(book_id)).first()

            if existing_book:
                for key, value in updated_book.items():
                    setattr(existing_book, key, value)
                existing_book.save()
                return jsonify({"message": "Data updated successfully"}), 200
            else:
                return jsonify({"error": "Data not found"}), 404
        else:
            return jsonify({"error": "Invalid JSON"}), 400
    except Exception as err:
        return jsonify({"error": str(err)}), 500

@app.route('/api/data/<book_id>', methods=['DELETE'])
def delete_data(book_id):
    try:
        book = Book.objects(id=book_id).first()

        if book:
            book.delete()
            return jsonify({"message": "Book deleted successfully"}), 200
        else:
            return jsonify({"error": "Data not found"}), 404
    except Exception as err:
        return jsonify({"error": str(err)}), 500


app.run(debug=True)