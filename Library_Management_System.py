class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.available = quantity  # for showing available books

books = []
# for issued books
issued_books = []

#for adding more new books
def add_book():
    book_id = input("Enter Book ID: ")
    #for checking for ID
    for book in books:
        if book.book_id == book_id:
            print("Book ID already exists!")
            return
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))
    # for Quantity
    if quantity <= 0:
        print("Quantity must be positive!")
        return
    new_book = Book(book_id, title, author, quantity)
    books.append(new_book)
    print("Book added successfully!")

#for showing all books
def view_books():
    if len(books) == 0:
        print("No books available!")
        return
    for book in books:
        print("ID:", book.book_id, "| Title:", book.title, "| Author:", book.author, "| Total:", book.quantity, "| Available:", book.available)

#for searching book with Title or ID
def search_book():
    search = input("Enter Book ID or Title: ")
    for book in books:
        if book.book_id == search or book.title.lower() == search.lower():
            print("ID:", book.book_id, "| Title:", book.title, "| Author:", book.author, "| Available:", book.available)
            return
    print("Book not found!")

#for issuing books
def issue_book():
    book_id = input("Enter Book ID: ")
    for book in books:
        if book.book_id == book_id:
            if book.available == 0:
                print("Book not available!")
                return
            student = input("Enter Student Name: ")
            book.available = book.available - 1
            issued_books.append({"book_id": book_id, "title": book.title, "student": student})
            print("Book issued successfully!")
            print("Available Quantity:", book.available)
            return
    print("Book not found!")

#for returning books
def return_book():
    book_id = input("Enter Book ID: ")
    student = input("Enter Student Name: ")
    for record in issued_books:
        if record["book_id"] == book_id and record["student"].lower() == student.lower():
            issued_books.remove(record)
            for book in books:
                if book.book_id == book_id:
                    book.available = book.available + 1
            print("Book returned successfully!")
            return
    print("No such issued record found!")

#for deleting books
def delete_book():
    book_id = input("Enter Book ID: ")
    for record in issued_books:
        if record["book_id"] == book_id:
            print("Cannot delete! Book is currently issued.")
            return
    for book in books:
        if book.book_id == book_id:
            books.remove(book)
            print("Book deleted successfully!")
            return
    print("Book not found!")

#for showing issued books
def view_issued_books():
    if len(issued_books) == 0:
        print("No books issued!")
        return
    for record in issued_books:
        print("Book ID:", record["book_id"], "| Title:", record["title"], "| Student:", record["student"])

#main menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        view_issued_books()
    elif choice == "8":
        print("Thank you! Program Closed.")
        break
    else:
        print("Invalid choice! Try again.")