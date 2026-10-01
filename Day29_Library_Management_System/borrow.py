class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True


class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book.title)
        else:
            print("Book is not available.")

    def show_member(self):
        print(f"Member Name: {self.name}")
        print(f"Member ID: {self.member_id}")
        print(f"Borrowed Books: {self.borrowed_books}")


book = Book(
    "Python Programming",
    "Mehedi Lipu",
    "9781234567890"
)

member = Member("Mehedi", "M001")
member.borrow_book(book)
member.show_member()

print("Book Available:", book.is_available)