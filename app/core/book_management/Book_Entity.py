from pydantic import BaseModel
from datetime import date
from models import ISBN

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
