from pydantic import BaseModel

# Value Object: ISBN
class ISBN(BaseModel):
    value: str

    def __init__(self, value: str):
        if len(value) != 13:
            raise ValueError("ISBN must be 13 characters long")
        self.value = value
