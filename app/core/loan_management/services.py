from .models import Loan

loans_db = []

def create_loan(loan: Loan):
    loans_db.append(loan)
    return loan

def get_loans():
    return loans_db
