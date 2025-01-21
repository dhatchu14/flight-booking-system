from models import Loan

class LoanAggregate:
    def __init__(self, loan: Loan):
        self.loan = loan

    def return_book(self):
        if self.loan.return_date is not None:
            raise ValueError("Book already returned")
        self.loan.mark_as_returned()
