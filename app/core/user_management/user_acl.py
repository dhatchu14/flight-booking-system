from .models import User
from .repositories import UserRepository
from .factories import UserFactory
from typing import Optional

class UserACL:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, username: str, email: str, password: str) -> User:
        # Check if the user already exists
        existing_user = self.user_repo.get_by_username(username)
        if existing_user:
            raise ValueError(f"User with username {username} already exists.")
        
        user = UserFactory.create_user(username=username, email=email, password=password)
        self.user_repo.add(user)
        return user

    def update_user(self, user_id: int, username: str, email: str) -> User:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        
        user.username = username
        user.email = email
        self.user_repo.update(user)
        return user

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repo.get_by_id(user_id)
