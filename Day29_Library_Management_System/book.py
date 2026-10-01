class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def show_book(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")

book = Book(
    "Python Programming",
    "Mehedi Lipu",
    "9781234567890"
)

book.show_book()