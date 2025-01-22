from fastapi import APIRouter
from .models import Loan
from .services import create_loan, get_loans

loan_router = APIRouter()

@loan_router.post("/")
def issue_loan(loan: Loan):
    return create_loan(loan)

@loan_router.get("/")
def list_loans():
    return get_loans()
