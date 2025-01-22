from .models import User

users_db = []

def create_user(user: User):
    users_db.append(user)
    return user

def get_users():
    return users_db
