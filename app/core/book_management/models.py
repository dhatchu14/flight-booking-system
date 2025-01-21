from pydantic import BaseModel
from datetime import date


# Value Object: ISBN
class ISBN(BaseModel):
    value: str

    ('value')
    def validate_isbn_length(cls, v):
        if len(v) != 13:
            raise ValueError("ISBN must be 13 characters long")
        return v


# Entity: Book
class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: ISBN
    available: bool = True

    def mark_as_unavailable(self):
        self.available = False

    def mark_as_available(self):
        self.available = True
