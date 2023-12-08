from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse
import json


class Book:
    def __init__(self, id, title, author, year, kind):
        self.id = id
        if len(title) == 0:
            raise Exception("There should be a title of the book!")
        self.title = title
        if len(author) == 0:
            raise Exception("There should be a author of the book!")
        self.author = author
        if year < 1900 or year > 2023:
            raise Exception("Year should be in range(1900; 2023)")
        self.year = year
        if len(kind) == 0:
            raise Exception("There should be a kind of the book!")
        self.kind = kind

    def encode(self):
        return self.__dict__


def get_books():
    books = []
    with open("data.json", "r") as j:
        datas = json.loads(j.read())
        for data in datas:
            books.append(Book(data["id"], data["title"], data["author"], data["year"], data["kind"]))
    return books


def write_books(books):
    with open("data.json", "w") as j:
        json.dump(books, j, default=lambda o: o.encode(), sort_keys=True)

# books = [Book(1,"Eat. Love. Pray.", "Elizabeth Gilbert", 2020, "romance"),
#             Book(2,"7 habits of great people", "Stiven Kovi", 2004, "psychology"),
#               Book(3,"Hobbit", "G.R. Talkien", 2013, "fantasy")]
# write_books(books)

def find_book(id):
    for b in get_books():
        if b.id == id:
            return b
    return None


app = FastAPI()


@app.get("/api/books")
def get_all_books():
    return get_books()


@app.get("/api/books/{id}")
def get_book(id):
    book = find_book(int(id))
    if book is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Book isn't found"}
        )
    return book


@app.post("/api/books")
def create_book(data=Body()):
    book = Book(data["id"], data["title"], data["author"], data["year"], data["kind"])
    if find_book(int(data["id"])) is not None:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": "Book with the same id already exists"}
        )
    books = get_books()
    books.append(book)
    write_books(books)
    return book


@app.patch("/api/books")
def edit_book(data=Body()):
    if find_book(int(data["id"])) is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Book isn't found"}
        )

    books = get_books()
    for b in books:
        if b.id ==int(data["id"]):
            b.title = data["title"]
            b.author = data["author"]
            b.year = data["year"]
            b.kind = data["kind"]
    write_books(books)
    return find_book(int(data["id"]))


@app.delete("/api/books/{id}")
def delete_book(id):
    if find_book(int(id)) is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Book isn't found"}
        )
    books = get_books()
    for b in books:
        if b.id == int(id):
            books.remove(b)
            write_books(books)
            return b
