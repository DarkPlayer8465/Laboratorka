# models/user.py
from dataclasses import dataclass

@dataclass
class User:
    username: str
    role: str
    password: str    # здесь хранится хеш пароля для входа