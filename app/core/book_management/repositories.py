from .models import Book
from typing import List

class BookRepository:
    def __init__(self):
        self.books = {}

    def add(self, book: Book):
        self.books[book.id] = book

    def get(self, book_id: int) -> Book:
        return self.books.get(book_id)

    def all(self) -> List[Book]:
        return list(self.books.values())
