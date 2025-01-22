from fastapi import APIRouter, HTTPException
from .models import Book
from .services import add_book, get_books, get_book

book_router = APIRouter()

@book_router.post("/")
def create_book(book: Book):
    return add_book(book)

@book_router.get("/")
def list_books():
    return get_books()

@book_router.get("/{book_id}")
def get_book_details(book_id: int):
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
