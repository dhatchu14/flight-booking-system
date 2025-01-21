from fastapi import APIRouter, HTTPException
from typing import List
from .models import Book
from .repositories import BookRepository
from .services import BookService

# Initialize the router for book routes
book_router = APIRouter()

# Instantiate the BookService and repository
book_repo = BookRepository()
book_service = BookService(book_repo)

@book_router.post("/books/", response_model=Book)
async def create_book(book: Book):
    try:
        return book_service.create_book(book)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@book_router.get("/books/", response_model=List[Book])
async def get_books():
    return book_service.get_all_books()

@book_router.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = book_service.get_book_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@book_router.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    try:
        return book_service.update_book(book_id, book)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@book_router.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int):
    try:
        book_service.delete_book(book_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
