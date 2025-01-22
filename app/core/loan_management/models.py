from typing import Optional
from pydantic import BaseModel
from datetime import date

class Loan(BaseModel):
    id: int
    book_id: int
    user_id: int
    loan_date: date
    return_date: Optional[date] = None
