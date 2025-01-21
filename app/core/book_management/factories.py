from datetime import date
from .models import Book, User, Loan,ISBN
from typing import Optional

class BookFactory:
    @staticmethod
    def create_book(title: str, author: str, isbn: str, available: bool = True) -> Book:
        # Create a new ISBN value object and pass it to the Book entity
        return Book(
            title=title,
            author=author,
            isbn=ISBN(value=isbn),  # Pass the 'isbn' string as 'value' to the ISBN constructor
            available=available
        )
