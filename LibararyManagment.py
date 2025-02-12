# Library Class
class Library:
    book_list = [] 

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)  

    @classmethod
    def view_book_info(cls):
        print("\nLibrary Books:")
        for book in cls.book_list:
            book.view_book_info()  

    @classmethod
    def find_book_by_id(cls, book_id):
        for book in cls.book_list:
            if book.id() == book_id:
                return book
        return None


# Book Class
class Book(Library):
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)  

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' has been borrowed successfully.")
        else:
            print(f"Book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"Book '{self.__title}' has been returned successfully.")
        else:
            print(f"Book '{self.__title}' was not borrowed.")

    def view_book_info(self):
        print(f"Book ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {'Available' if self.__availability else 'Not Available'}")

    def id(self):
        return self.__book_id

    def book_name(self):
        return self.__title

    def author_name(self):
        return self.__author

    def availability(self):
        return self.__availability



Book(101, "Python Programming", "John Doe", True)
Book(102, "Clean Code", "Robert C. Martin", True)
Book(103, "The Pragmatic Programmer", "Andrew Hunt and David Thomas", True)
Book(104, "Design Patterns", "Erich Gamma et al.", True)
Book(105, "Introduction to Algorithms", "Thomas H. Cormen", True)
Book(106, "You Don't Know JS", "Kyle Simpson", True)
Book(107, "The Art of Computer Programming", "Donald E. Knuth", True)
Book(108, "Head First Java", "Kathy Sierra and Bert Bates", True)
Book(109, "Effective Java", "Joshua Bloch", True)
Book(110, "Code Complete", "Steve McConnell", True)



def switch(option):
    if option == "1":
        Library.view_book_info()  
    elif option == "2":
        book_id = int(input("Enter book ID to borrow: ")) 
        book = Library.find_book_by_id(book_id)
        if book:
            book.borrow_book()  
        else:
            print("Invalid book ID.")
    elif option == "3":
        book_id = int(input("Enter book ID to return: "))  
        book = Library.find_book_by_id(book_id)
        if book:
            book.return_book() 
        else:
            print("Invalid book ID.")
    elif option == "4":
        return True
    else:
        print("Invalid option. Please try again.")
    return False


# Main loop
while True:
    print("\n----- Welcome to the Library -----")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit\n")

    option = input("Enter your choice: ")
    if switch(option):
        break