# solution

```python
# -----------------------------
# Library Management System
# -----------------------------

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.book_id} | {self.title} | {self.author} | {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("\nBook added successfully!\n")

    def view_books(self):
        if not self.books:
            print("\nNo books available.\n")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            print(book)
        print()

    def search_book(self, keyword):
        found = [b for b in self.books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]
        
        if not found:
            print("\nNo matching books found.\n")
            return
        
        print("\n--- Search Results ---")
        for b in found:
            print(b)
        print()

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print("\nBook borrowed successfully!\n")
                else:
                    print("\nBook is already borrowed.\n")
                return
        print("\nBook ID not found.\n")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print("\nBook returned successfully!\n")
                else:
                    print("\nThis book was not borrowed.\n")
                return
        print("\nBook ID not found.\n")


# -----------------------------
# CLI Menu
# -----------------------------

def menu():
    print("""
===== Library Management System =====

1. Add Book
2. View Books
3. Search Book
4. Borrow Book
5. Return Book
6. Exit

====================================
""")

def main():
    library = Library()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.add_book(Book(book_id, title, author))

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            keyword = input("Enter title/author keyword to search: ")
            library.search_book(keyword)

        elif choice == "4":
            book_id = input("Enter Book ID to borrow: ")
            library.borrow_book(book_id)

        elif choice == "5":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == "6":
            print("\nThank you for using Library Management System!\n")
            break

        else:
            print("\nInvalid choice, try again.\n")


# Run Program
if __name__ == "__main__":
    main()
```
