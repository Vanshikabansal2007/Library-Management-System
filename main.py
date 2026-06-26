class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
      
    def display_book(self):
        print("Book ID:" ,self.book_id)
        print("Title:" ,self.title)
        print("Author:" ,self.author)
        print("Available:" ,self.is_available)  
    
        
book1 = Book(101, "Python Programming", "Vanshika")
book2 = Book(102, "Data Structures", "Aditya")
book3 = Book(103, "Machine Learning", "Riya")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
      
    def display_member(self):
        print("Member ID:" ,self.member_id)
        print("Name:" ,self.name)
        print("Borrowed Books:")
        
        if len(self.borrowed_books) == 0:
            print("No books borrowed.")
        
        for book in self.borrowed_books:
            print(book.title)
            
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        
    def add_book(self, book):
        self.books.append(book)
        print(book.title, "has been added to the library.")
        
    def add_member(self, member):
        self.members.append(member)
        print(member.name, "has been added as a member.")
        
    def show_books(self):
        print("Books in the library:")
        for book in self.books:
            book.display_book()
            print()
            
    def show_members(self):
        print("Library Members:")
        for member in self.members:
            member.display_member()
            print()
            
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print("Book found:")
                book.display_book()
                return
        print("Book not found.")
        
    def issue_book(self, member_id, book_id):
        member = None
        
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
            
        book = None
        
        for b in self.books:
            if b.book_id == book_id:
                book = b
                break
            
        if member is None:
            print("Member not found.")
            return
        if book is None:
            print("Book not found.")
            return
        if book.is_available:
            member.borrowed_books.append(book)
            book.is_available = False
            print(book.title, "has been issued to", member.name)
        else:
            print("Book is already issued.")
            
    def return_book(self, member_id, book_id):

        member = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if member is None:
                print("Member not found.")
                return

        for book in member.borrowed_books:

            if book.book_id == book_id:

                member.borrowed_books.remove(book)

                book.is_available = True

                print(book.title, "has been returned successfully.")

                return

        print("This member has not borrowed this book.")
            
library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

member1 = Member(1, "Vanshika")
member2 = Member(2, "Rahul")
member3 = Member(3, "Priya")

library.add_member(member1)
library.add_member(member2)
library.add_member(member3)
"""
library.show_books()

library.show_members()
library.search_book("Data Structures")

library.issue_book(1, 102)

print("\nAfter Issuing Book")
library.show_members()
library.show_books()

library.return_book(1, 102)

print("\nAfter Returning Book")
library.show_members()
library.show_books()
"""


while True:

    print("Welcome to the Library Management System!!")
    print("1. Show Books")
    print("2. Show Members")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        library.show_books()
    elif choice == '2':
        library.show_members()
    elif choice == '3':
        title = input("Enter the title of the book to search: ")
        library.search_book(title)
    elif choice == '4':
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        library.issue_book(member_id, book_id)
    elif choice == '5':
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        library.return_book(member_id, book_id)
    elif choice == '6':
        print("Thank you for using the Library Management System!")
        break
    else:
        print("Invalid choice. Please try again.")