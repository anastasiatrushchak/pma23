from flask import Flask, jsonify, request
import json

app = Flask(__name__)
file_path = "books_data.json"
class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def to_dict(self):
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year
        }
def read_data():
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            books = [Book(book["id"], book["title"], book["author"], book["year"]) for book in data]
        return books
    except FileNotFoundError:
        return []

def write_data(books):
    data = [book.to_dict() for book in books]
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

@app.route('/books', methods=['GET'])
def get_books():
    books = read_data()
    return jsonify([book.to_dict() for book in books])
@app.route('/books', methods=['POST'])
def add_books():
    new_books_data = request.json
    existing_books = read_data()
    new_books = []
    max_id = max([book.book_id for book in existing_books]) if existing_books else 0
    for book_data in new_books_data:
        max_id += 1
        new_book = Book(max_id, book_data.get('title'), book_data.get('author'), book_data.get('year'))
        new_books.append(new_book)

    existing_books.extend(new_books)
    write_data(existing_books)

    return jsonify([book.to_dict() for book in new_books]), 201

@app.route('/books/<int:book_id>', methods=['PATCH'])
def update_book(book_id):
    books = read_data()
    book = next((b for b in books if b.book_id == book_id), None)
    if book:
        data = request.json
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.year = data.get('year', book.year)
        write_data(books)
        return jsonify(book.to_dict())
    return jsonify({"message": "Book not found"}), 404
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    books = read_data()
    books = [b for b in books if b.book_id != book_id]
    write_data(books)
    return jsonify({"message": "Book deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
