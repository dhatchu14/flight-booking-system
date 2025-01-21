from fastapi import APIRouter, HTTPException
from typing import List

# Importing models and services
from app.core.book_management.models import Book  # Assuming this is where Book is defined
from app.core.loan_management.models import Loan  # Assuming this is where Loan is defined
from app.core.user_management.models import User  # Assuming this is where User is defined

from app.core.book_management.services import BookService
from app.core.loan_management.services import LoanService
from app.core.user_management.services import UserService

# Instantiate the services
book_service = BookService()
loan_service = LoanService()
user_service = UserService()

# Initialize the router
router = APIRouter()

# Book Management Routes
@router.post("/books/", response_model=Book)
async def create_book(book: Book):
    try:
        return await book_service.create_book(book)  # Assuming this is an async function
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/books/", response_model=List[Book])
async def get_books():
    return await book_service.get_all_books()  # Assuming this is an async function


@router.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = await book_service.get_book_by_id(book_id)  # Assuming this is an async function
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    try:
        return await book_service.update_book(book_id, book)  # Assuming this is an async function
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int):
    try:
        await book_service.delete_book(book_id)  # Assuming this is an async function
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# User Management Routes
@router.post("/users/", response_model=User)
async def create_user(user: User):
    try:
        return await user_service.create_user(user)  # Assuming this is an async function
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = await user_service.get_user(user_id)  # Assuming this is an async function
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    try:
        return await user_service.update_user(user_id, user)  # Assuming this is an async function
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    try:
        await user_service.delete_user(user_id)  # Assuming this is an async function
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Loan Management Routes
@router.post("/loans/", response_model=Loan)
async def create_loan(book_id: int, user_id: int, due_date: str):
    try:
        return await loan_service.create_loan(book_id, user_id, due_date)  # Assuming this is an async function
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/loans/{loan_id}", response_model=Loan)
async def get_loan(loan_id: int):
    loan = await loan_service.get_loan_by_id(loan_id)  # Assuming this is an async function
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan


@router.get("/users/{user_id}/loans", response_model=List[Loan])
async def get_user_loans(user_id: int):
    return await loan_service.get_user_loans(user_id)  # Assuming this is an async function


@router.put("/loans/{loan_id}/return", response_model=Loan)
async def return_book(loan_id: int, return_date: str):
    try:
        return await loan_service.return_book(loan_id, return_date)  # Assuming this is an async function
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
