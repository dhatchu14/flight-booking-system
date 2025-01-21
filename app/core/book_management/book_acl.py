from .models import Book
from .repositories import BookRepository

class BookACL:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def get_book_by_isbn(self, isbn: str) -> Book:
        book = self.book_repo.get_by_isbn(isbn)
        if not book:
            raise ValueError("Book not found")
        return book

    def add_book(self, title: str, author: str, isbn: str) -> Book:
        existing_book = self.book_repo.get_by_isbn(isbn)
        if existing_book:
            raise ValueError("Book with this ISBN already exists")
        book = Book(title=title, author=author, isbn=isbn)
        self.book_repo.add(book)
        return book
