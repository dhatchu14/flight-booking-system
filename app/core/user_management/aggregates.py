from typing import List
from .models import User

class UserAggregate:
    def __init__(self, user: User):
        self.user = user
        self.borrowed_books: List[int] = user.borrowed_books

    def borrow_book(self, book_id: int):
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
        else:
            raise ValueError("This book is already borrowed by the user")

    def return_book(self, book_id: int):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
        else:
            raise ValueError("This book is not borrowed by the user")

    def update_user_details(self, username: str, email: str):
        self.user.username = username
        self.user.email = email

    def get_user(self) -> User:
        self.user.borrowed_books = self.borrowed_books
        return self.user
