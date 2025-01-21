from fastapi import FastAPI
from app.api.routes import router
from app.core.book_management.services import BookService
from app.core.user_management.services import UserService
from app.core.loan_management.services import LoanService



app = FastAPI()

# Include all the routes in the app
app.include_router(router, prefix="/api", tags=["Library Management"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Library Management System API"}
