class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print("Patron registered successfully.")

    def borrow_book(self, book_id, patron_id):
        book = None
        patron = None

        for b in self.books:
            if b.book_id == book_id:
                book = b

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p

        if book is None:
            print("Book not found.")
            return

        if patron is None:
            print("Patron not found.")
            return

        if book.is_borrowed:
            print("Book is already borrowed.")
            return

        book.is_borrowed = True
        patron.borrowed_books.append(book)
        print("Book borrowed successfully.")

    def return_book(self, book_id, patron_id):
        patron = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p

        if patron is None:
            print("Patron not found.")
            return

        for book in patron.borrowed_books:
            if book.book_id == book_id:
                book.is_borrowed = False
                patron.borrowed_books.remove(book)
                print("Book returned successfully.")
                return

        print("This book was not borrowed by this patron.")

    def display_books(self):
        print("\n--- Library Books ---")

        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"ID: {book.book_id}, Title: {book.title}, "
                  f"Author: {book.author}, Status: {status}")


# Creating Library object
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        library.register_patron(patron)

    elif choice == "3":
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        library.borrow_book(book_id, patron_id)

    elif choice == "4":
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        library.return_book(book_id, patron_id)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
