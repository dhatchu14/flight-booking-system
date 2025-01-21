from .models import Book

class BookAggregate:
    def __init__(self, book: Book):
        self.book = book

    def borrow(self):
        if not self.book.available:
            raise ValueError("Book is not available")
        self.book.mark_as_unavailable()

    def return_book(self):
        self.book.mark_as_available()
