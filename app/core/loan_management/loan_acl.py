from datetime import date
from .models import Loan
from .repositories import LoanRepository
from .factories import LoanFactory
from typing import Optional

class LoanACL:
    def __init__(self, loan_repo: LoanRepository):
        self.loan_repo = loan_repo

    def create_loan(self, book_id: int, user_id: int, due_date: date) -> Loan:
        # Check if the book is available (example: add additional rules or validation logic)
        existing_loan = self.loan_repo.get_active_loan_by_user(user_id)
        if existing_loan:
            raise ValueError(f"User already has an active loan for this book.")
        
        loan = LoanFactory.create_loan(book_id=book_id, user_id=user_id, due_date=due_date)
        self.loan_repo.add(loan)
        return loan

    def return_book(self, loan_id: int, return_date: date) -> Loan:
        loan = self.loan_repo.get_by_id(loan_id)
        if loan is None:
            raise ValueError(f"Loan not found.")
        
        loan.return_book(return_date)
        self.loan_repo.update(loan)
        return loan

    def get_user_loans(self, user_id: int) -> Optional[list]:
        return self.loan_repo.get_loans_by_user(user_id)
