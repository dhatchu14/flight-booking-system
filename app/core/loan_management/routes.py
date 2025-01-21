from fastapi import APIRouter, HTTPException
from typing import List
from .models import Loan
from .repositories import LoanRepository
from .services import LoanService

# Initialize the router for loan routes
loan_router = APIRouter()

# Instantiate the LoanService and repository
loan_repo = LoanRepository()
loan_service = LoanService(loan_repo)

@loan_router.post("/loans/", response_model=Loan)
async def create_loan(book_id: int, user_id: int, due_date: str):
    try:
        return loan_service.create_loan(book_id, user_id, due_date)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@loan_router.get("/loans/{loan_id}", response_model=Loan)
async def get_loan(loan_id: int):
    loan = loan_service.get_loan_by_id(loan_id)
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan

@loan_router.get("/users/{user_id}/loans", response_model=List[Loan])
async def get_user_loans(user_id: int):
    return loan_service.get_user_loans(user_id)

@loan_router.put("/loans/{loan_id}/return", response_model=Loan)
async def return_book(loan_id: int, return_date: str):
    try:
        return loan_service.return_book(loan_id, return_date)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
