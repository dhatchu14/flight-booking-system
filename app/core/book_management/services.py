from .models import Book

books_db = []

def add_book(book: Book):
    books_db.append(book)
    return book

def get_books():
    return books_db

def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    return None
