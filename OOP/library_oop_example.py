class Library:
    def __init__(self, listOfBooks):
        self.listOfBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        for book in self.listOfBooks:
            print(book)
        print()

    def lendBook(self, requestedBook):
        if requestedBook in self.listOfBooks:
            print("You have now borrowed the book")
            self.listOfBooks.remove(requestedBook)
        else:
            print("Sorry the book is not available in our list.")
    def addBook(self, returnedBook):
        self.listOfBooks.append(returnedBook)
        print("You have returned the book. Thank you!")


class Customer:
    def requestBook(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book

library = Library(['Think and Grow Rich', 'Who Will Cry When You Die','For One More Day'])
customer = Customer()

while True:
    print("1. To display the available books")
    print("2. To request a book")
    print("3. To return a book")
    print("4. To exit")
    userChoice = int(input())


    if userChoice == 1:
        library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        quit()
