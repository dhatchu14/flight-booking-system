from datetime import date
from typing import List

# Domain Event for Book Management
class BookCreated:
    def __init__(self, book_id: int, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author

class BookUpdated:
    def __init__(self, book_id: int, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        