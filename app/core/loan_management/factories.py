from datetime import date
from .models import Book, User, Loan
from typing import Optional

# Factory for Loan Management
class LoanFactory:
    @staticmethod
    def create_loan(book: Book, user: User, due_date: date) -> Loan:
        return Loan(book=book, user=user, due_date=due_date)