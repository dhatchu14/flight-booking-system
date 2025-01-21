from .aggregates import LoanAggregate
from .repositories import LoanRepository
from datetime import date

class LoanService:
    def __init__(self, loan_repo: LoanRepository, book_repo):
        self.loan_repo = loan_repo
        self.book_repo = book_repo

    def borrow_book(self, user_id: int, book_id: int):
        book = self.book_repo.get(book_id)
        loan = Loan(id=len(self.loan_repo.loans) + 1, user_id=user_id, book_id=book_id, borrow_date=date.today(), due_date=date.today())
        loan_aggregate = LoanAggregate(loan)
        loan_aggregate.borrow()
        self.loan_repo.add(loan)
        return loan

    def return_book(self, loan_id: int):
        loan = self.loan_repo.get(loan_id)
        loan_aggregate = LoanAggregate(loan)
        loan_aggregate.return_book()
        return loan
