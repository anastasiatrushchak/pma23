class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - {self.genre}"

b1 = Book("Cosmic Chronicles", "Faye Galaxy", 2019, "science fiction")
b2 = Book("Deep Thoughts", "Phil O'Sophy", 2015, "philosophy")
b3 = Book("Enchanted Forest", "Elle Woods", 2018, "fantasy")

books = {
    "CosmicChronicles": b1,
    "DeepThoughts": b2,
    "EnchantedForest": b3
}

def display_books(books_dict):
    for book_id, book in books_dict.items():
        print(f"{book_id}: {book}")

print("Original list of books:")
display_books(books)
print()

books["CosmicChronicles"].year = 2021

books["EnchantedForest"] = Book("Enchanted Forest II", "Elle Woods", 2020, "fantasy novel")

books.pop("DeepThoughts", None)

print("Updated list of books:")
display_books(books)
print()
