class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        
    
    def __len__(self):
        return self.pages

book1 = Book("Python Basics", 250)

print(len(book1))