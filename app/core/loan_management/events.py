from datetime import date
from typing import List

# Domain Event for Loan Management
class LoanCreated:
    def __init__(self, loan_id: int, user_id: int, book_id: int, due_date: date):
        self.loan_id = loan_id
        self.user_id = user_id
        self.book_id = book_id
        self.due_date = due_date

class LoanReturned:
    def __init__(self, loan_id: int, return_date: date):
        self.loan_id = loan_id
        self.return_date = return_date