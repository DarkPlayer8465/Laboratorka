# services/user_service.py
import hashlib
from repositories import user_repository
from models.user import User

ADMIN_ROLE = "admin"
USER_ROLE = "user"

def _hash(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def register(username: str, password: str, role: str = USER_ROLE):
    username = username.strip()
    if not username:
        raise Exception("Имя пользователя не может быть пустым")
    if len(password) < 4:
        raise Exception("Пароль должен содержать минимум 4 символа")
    if role not in (ADMIN_ROLE, USER_ROLE):
        raise Exception("Неизвестная роль")
    if user_repository.get_by_username(username):
        raise Exception("Пользователь с таким именем уже существует")
    user_repository.create(username, role, _hash(password))

def authenticate(username: str, password: str) -> User | None:
    user = user_repository.get_by_username(username.strip())
    if user and user.password == _hash(password):
        return user
    return None

def ensure_default_admin():
    """Если пользователей нет, создаём первого администратора: admin / admin."""
    if user_repository.count() == 0:
        register("admin", "admin", ADMIN_ROLE)