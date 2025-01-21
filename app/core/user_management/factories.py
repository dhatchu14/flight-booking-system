from datetime import date
from .models import Book, User, Loan
from typing import Optional

class UserFactory:
    @staticmethod
    def create_user(username: str, email: str, password: str) -> User:
        return User(username=username, email=email, password=password)