from fastapi import APIRouter, HTTPException
from .models import User
from .repositories import UserRepository
from .services import UserService

# Initialize the router for user routes
user_router = APIRouter()

# Instantiate the UserService and repository
user_repo = UserRepository()
user_service = UserService(user_repo)

@user_router.post("/users/", response_model=User)
async def create_user(user: User):
    try:
        return user_service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    try:
        return user_service.update_user(user_id, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    try:
        user_service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
