from typing import List, Optional
from .models import User
from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> User:
        """Add a new user to the repository."""
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Fetch a user by their ID."""
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        """Update an existing user in the repository."""
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        """Delete a user by their ID."""
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        """Get all users."""
        pass

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}
        self.counter = 1

    def add(self, user: User) -> User:
        user.id = self.counter
        self.users[self.counter] = user
        self.counter += 1
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    def update(self, user: User) -> User:
        if user.id in self.users:
            self.users[user.id] = user
            return user
        else:
            raise ValueError("User not found")

    def delete(self, user_id: int) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def get_all(self) -> List[User]:
        return list(self.users.values())
