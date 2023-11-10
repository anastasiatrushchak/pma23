class Book:
    def __init__(self, title, author, year, kind):
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

    def __str__(self):
        return f'Title: {self.title}, \nAuthor: {self.author}, \nYear: {self.year}, \nType: {self.kind}'
