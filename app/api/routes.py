from fastapi import APIRouter
from core.book_management.book_acl import book_router
from core.loan_management.loan_acl import loan_router
from core.user_management.user_acl import user_router

router = APIRouter()

router.include_router(book_router, prefix="/books", tags=["Books"])
router.include_router(loan_router, prefix="/loans", tags=["Loans"])
router.include_router(user_router, prefix="/users", tags=["Users"])
