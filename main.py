class Library:
    # Class variable for books
    books = []
    
    # Constructor
    def __init__(self, bookList):
        self.books = bookList
    
    # Display books
    def display(self):
        for i in self.books:
            print(i)

    # borrow book
    def borrow(self, book):
        if book in self.books:
            self.books.remove(book)
            print("You have borrowed", book)
        else:
            print("The book is not available")


# Main
bookList = ["The Great Gatsby", "1947", "Pride and Prejudice"]

# Create Object
library = Library(bookList)

while True:
    print("\n--- Library Menu ---")
    print("1. Display Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")
    
    choice = input("Enter The Choice {1/2/3/4}: ")

    if choice == "1":
        library.display()
    elif choice == "2":
        book = input("Enter the book you want to borrow: ")
        library.borrow(book)
    elif choice == "4":
        break
    else:
        print("Please choose a valid option")
