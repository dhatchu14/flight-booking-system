from pydantic import BaseModel
from datetime import date

class Loan(BaseModel):
    id: int
    user_id: int
    book_id: int
    borrow_date: date
    due_date: date
    return_date: date = None

    def mark_as_returned(self):
        self.return_date = date.today()
