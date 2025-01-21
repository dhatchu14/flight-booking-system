from .models import Loan
from typing import List

class LoanRepository:
    def __init__(self):
        self.loans = {}

    def add(self, loan: Loan):
        self.loans[loan.id] = loan

    def get(self, loan_id: int) -> Loan:
        return self.loans.get(loan_id)

    def all(self) -> List[Loan]:
        return list(self.loans.values())
