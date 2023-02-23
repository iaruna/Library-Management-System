'''Library Management System!'''

class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Harry Potter")
l1.addBook("Making India Awesome")
l1.addBook("One Indian Girl")
l1.addBook("Half Girlfriend")
l1.addBook("Revolution 2020")
l1.addBook("Naked Triangle")
l1.addBook("A Million Mutinies Now")
l1.addBook("A Bend in the River")
l1.addBook("A Brush with Life")
l1.addBook("A Passage to England")
l1.showInfo()




