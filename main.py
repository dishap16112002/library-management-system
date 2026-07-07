
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        if book_id in self.books:
            print("❌ Book ID already exists!")
        else:
            self.books[book_id] = {
                "title": title,
                "author": author,
                "available": True,
                "student": ""
            }
            print("✅ Book Added Successfully!")

    def view_books(self):
        if not self.books:
            print("❌ No Books Available!")
            return

        print("\n========== BOOK LIST ==========")

        for book_id, book in self.books.items():
            status = "Available" if book["available"] else "Issued"

            print("----------------------------")
            print("Book ID :", book_id)
            print("Title   :", book["title"])
            print("Author  :", book["author"])
            print("Status  :", status)

    def search_book(self):
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            book = self.books[book_id]

            print("\n========== BOOK DETAILS ==========")
            print("Book ID :", book_id)
            print("Title   :", book["title"])
            print("Author  :", book["author"])
            print("Status  :", "Available" if book["available"] else "Issued")
        else:
            print("❌ Book Not Found!")
    def    issue_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("❌ Book Not Found!")
            return

        if not self.books[book_id]["available"]:
            print("❌ Book Already Issued!")
            return

        student = input("Enter Student Name: ")

        self.books[book_id]["available"] = False
        self.books[book_id]["student"] = student

        print("✅ Book Issued Successfully!")

    def return_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("❌ Book Not Found!")
            return

        if self.books[book_id]["available"]:
            print("❌ Book Is Already Available!")
            return

        self.books[book_id]["available"] = True
        self.books[book_id]["student"] = ""

        print("✅ Book Returned Successfully!")

    def issued_books(self):
        found = False

        print("\n========== ISSUED BOOKS ==========")

        for book_id, book in self.books.items():

            if not book["available"]:
                print("----------------------------")
                print("Book ID :", book_id)
                print("Title   :", book["title"])
                print("Student :", book["student"])
                found = True

        if not found:
            print("No Issued Books!")

    def delete_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("❌ Book Not Found!")
            return

        if not self.books[book_id]["available"]:
            print("❌ Cannot Delete Issued Book!")
            return

        del self.books[book_id]

        print("✅ Book Deleted Successfully!")
library  =  Library()

while True:
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. View Issued Books")
    print("7. Delete Book")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.issued_books()

    elif choice == "7":
        library.delete_book()

    elif choice == "8":
        print("🙏 Thank You for Using Library Management System!")
        break

    else:
        print("❌ Invalid Choice! Please Try Again.")              