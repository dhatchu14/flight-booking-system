from fastapi import APIRouter
from .models import User
from .services import create_user, get_users

user_router = APIRouter()

@user_router.post("/")
def register_user(user: User):
    return create_user(user)

@user_router.get("/")
def list_users():
    return get_users()
