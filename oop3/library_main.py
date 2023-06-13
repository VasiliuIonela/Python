
from oop3.library  import Book
from oop3.library import Member
from oop3.library import Library


book1 = Book('1984', 'George Orwell', 1949)
book2 = Book('Pride and prejudice', 'Jane Austen', 1813)
book3 = Book('Crime and punishment', 'Fyodor Dostoevsky', 1866)
book4 = Book('Harry Potter', 'J. K. Rowling', 1997)
book5 = Book("Narnia's Chronicle", 'C. S Lewis', 1950)

book1.add_book(1)
book2.add_book(2)
book3.add_book(3)
book4.add_book(4)
book5.add_book(5)

b1 = Library()
b2 = Library()
b1.borrow_book()
b1.borrow_book()
b1.return_book()
b1.borrow_book()

m1 = Member('Ionela')
m1.borrowed_books()
m1.borrowed_books()

