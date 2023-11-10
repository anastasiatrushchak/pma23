from book import Book
try:
    books = {"EatLovePray": Book("Eat. Love. Pray.", "Elizabeth Gilbert", 2020, "romance"),
             "7 habits of great people": Book("7 habits of great people", "Stiven Kovi", 2004, "psychology"),
             "Hobbit": Book("Hobbit", "G.R. Talkien", 2013, "fantasy")}
    for i in books:
        print(i, books[i], sep="\n")
        print()

    books["EatLovePray"].year = 2021
    books["Hobbit"] = Book("Hobbit", "G.R. Tolkien", 2015, "fantasy novel")
    books.pop("7 habits of great people")
    print("---------------------------")
    for i in books:
        print(i, books[i], sep="\n")
        print()
except Exception as e:
    print(e)
