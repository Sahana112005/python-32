class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  

    def display_details(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"📖 '{self.title}' by {self.author} [{status}]")
class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Added to inventory: '{book.title}'")

    def show_catalog(self):
        print(f"\n--- {self.name} Catalog ---")
        if not self.books:
            print("The library is currently empty.")
            return
        for book in self.books:
            book.display_details()
        print("-" * 30)

    def lend_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"📤 Success! You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"❌ Sorry, '{book.title}' is already checked out.")
                    return
        print(f"🔍 Sorry, '{book_title}' is not in our collection.")
my_library = Library("City Central Library")
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("1984", "George Orwell")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.show_catalog()
my_library.lend_book("1984")
my_library.lend_book("1984")
my_library.show_catalog()
