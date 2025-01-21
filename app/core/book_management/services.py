from datetime import date
from typing import List
from .models import Book, ISBN
from .repositories import BookRepository

class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def add_book(self, book: Book) -> Book:
        # Add a new book to the system
        return self.book_repository.add(book)

    def update_book(self, book_id: int, updated_book: Book) -> Book:
        # Update book details by ID
        existing_book = self.book_repository.get_by_id(book_id)
        if existing_book:
            existing_book.title = updated_book.title
            existing_book.author = updated_book.author
            existing_book.isbn = updated_book.isbn
            existing_book.category = updated_book.category
            return self.book_repository.update(existing_book)
        else:
            raise ValueError("Book not found")

    def delete_book(self, book_id: int) -> bool:
        # Delete a book by ID
        return self.book_repository.delete(book_id)

    def get_all_books(self) -> List[Book]:
        # Fetch all books
        return self.book_repository.get_all()

    def get_book_by_isbn(self, isbn: ISBN) -> Book:
        # Fetch a book by ISBN
        return self.book_repository.get_by_isbn(isbn)

    def check_availability(self, book_id: int) -> bool:
        # Check if the book is available (not loaned)
        book = self.book_repository.get_by_id(book_id)
        return book and book.is_available()

