# repositories/player_repository.py
from database.database import get_connection
from models.player import Player

_SELECT = '''
    SELECT p."id", p."имя_игрока", p."позиция", p."команда_id",
           c."название_команды", t."название"
    FROM "составы" p
    JOIN "команды" c ON c."id" = p."команда_id"
    JOIN "турниры" t ON t."id" = c."турнир_id"
'''

def _map(row) -> Player:
    return Player(*row)

def create(name: str, position: str, team_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO "составы"("имя_игрока", "позиция", "команда_id") VALUES (?, ?, ?)',
        (name, position, team_id),
    )
    conn.commit()
    conn.close()

def get_by_id(player_id: int) -> Player | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(_SELECT + ' WHERE p."id" = ?', (player_id,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None

def get_all() -> list[Player]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(_SELECT + ' ORDER BY t."название", c."название_команды", p."имя_игрока"')
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]

def get_by_team(team_id: int) -> list[Player]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        _SELECT + ' WHERE p."команда_id" = ? ORDER BY p."имя_игрока"', (team_id,)
    )
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]

def count_by_team(team_id: int) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM "составы" WHERE "команда_id" = ?', (team_id,))
    count = cur.fetchone()[0]
    conn.close()
    return count

def update(player_id: int, name: str, position: str, team_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        '''UPDATE "составы"
           SET "имя_игрока" = ?, "позиция" = ?, "команда_id" = ?
           WHERE "id" = ?''',
        (name, position, team_id, player_id),
    )
    conn.commit()
    conn.close()

def delete(player_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM "составы" WHERE "id" = ?', (player_id,))
    conn.commit()
    conn.close()