# repositories/tournament_repository.py
from database.database import get_connection
from models.tournament import Tournament

_SELECT = '''SELECT "id", "название", "спорт" FROM "турниры"'''

def _map(row) -> Tournament:
    return Tournament(*row)

def create(name: str, sport: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO "турниры"("название", "спорт") VALUES (?, ?)', (name, sport)
    )
    conn.commit()
    conn.close()

def get_by_id(tournament_id: int) -> Tournament | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(_SELECT + ' WHERE "id" = ?', (tournament_id,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None

def get_all() -> list[Tournament]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(_SELECT + ' ORDER BY "название"')
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]

def update(tournament_id: int, name: str, sport: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE "турниры" SET "название" = ?, "спорт" = ? WHERE "id" = ?',
        (name, sport, tournament_id),
    )
    conn.commit()
    conn.close()

def delete(tournament_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM "турниры" WHERE "id" = ?', (tournament_id,))
    conn.commit()
    conn.close()