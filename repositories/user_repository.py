# repositories/user_repository.py
from database.database import get_connection
from models.user import User

_SELECT = 'SELECT "имя_пользователя", "роль", "пароль" FROM "авторизация"'

def _map(row) -> User:
    return User(*row)

def create(username: str, role: str, password: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO "авторизация"("имя_пользователя", "роль", "пароль") VALUES (?, ?, ?)',
        (username, role, password),
    )
    conn.commit()
    conn.close()

def get_by_username(username: str) -> User | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(_SELECT + ' WHERE "имя_пользователя" = ?', (username,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None

def count() -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM "авторизация"')
    n = cur.fetchone()[0]
    conn.close()
    return n