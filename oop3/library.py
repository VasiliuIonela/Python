class Library:
    def __init__(self):
        self.available = True

    def borrow_book(self, ):
        if self.available:
            print(f'Book can be borrowed')
            self.available = False
        else:
            print(f'Book  is not available for the moment.')

    def return_book(self):
        print('Thank you, have a nice day.')
        self.available = True

class Member:
    def __init__(self, member_name):
        self.member_name = member_name
        self.books = 0

    def borrowed_books(self):
        self.books = self.books + 1
        print(' a mai imprumutat o carte')
        print(f'{self.member_name} are {self.books} carti imprumutate')
class Book:
    def __init__(self, book_name, author, year):
        self.book_name = book_name
        self.author = author
        self.year = year
        self.book_id = 0
    def add_book(self, id):
        self.hello()
        self.book_id = id
        print(f'Book name is: {self.book_name}')
        print(f'Author is: {self.author}')
        print(f'Year of appearence is: {self.year}')
        print(f'book id is: {self.book_id}')
        print('This book was successfully added to the library.')
        print('-------------------')

    def hello(self):
        print('Hello')

