from typing import List
from .models import User
from .repositories import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User) -> User:
        # Create a new user account
        return self.user_repository.add(user)

    def update_user(self, user_id: int, updated_user: User) -> User:
        # Update user details
        existing_user = self.user_repository.get_by_id(user_id)
        if existing_user:
            existing_user.username = updated_user.username
            existing_user.email = updated_user.email
            return self.user_repository.update(existing_user)
        else:
            raise ValueError("User not found")

    def delete_user(self, user_id: int) -> bool:
        # Delete a user by ID
        return self.user_repository.delete(user_id)

    def get_all_users(self) -> List[User]:
        # Fetch all users
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        # Fetch user by ID
        return self.user_repository.get_by_id(user_id)

    def borrow_book(self, user_id: int, book_id: int):
        # Allow a user to borrow a book
        user = self.user_repository.get_by_id(user_id)
        if user:
            user.borrow_book(book_id)
            self.user_repository.update(user)
        else:
            raise ValueError("User not found")

    def return_book(self, user_id: int, book_id: int):
        # Allow a user to return a book
        user = self.user_repository.get_by_id(user_id)
        if user:
            user.return_book(book_id)
            self.user_repository.update(user)
        else:
            raise ValueError("User not found")
