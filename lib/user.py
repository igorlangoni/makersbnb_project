from dataclasses import dataclass


@dataclass
class User:
    """Base Userclass"""

    id: int
    email: str
    username: str
    password: str

    def __repr__(self):
        return f"{self.id}, {self.email}, {self.username}, {self.password}"
