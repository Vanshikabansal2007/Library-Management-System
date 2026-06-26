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