# repositories/team_repository.py
from database.database import get_connection
from models.team import Team

_SELECT = '''
    SELECT c."id", c."название_команды", c."турнир_id", t."название"
    FROM "команды" c
    JOIN "турниры" t ON t."id" = c."турнир_id"
'''

def _map(row) -> Team:
    return Team(*row)

def create(name: str, tournament_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO "команды"("название_команды", "турнир_id") VALUES (?, ?)',
        (name, tournament_id),
    )
    conn.commit()
    conn.close()

def get_by_id(team_id: int) -> Team | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(_SELECT + ' WHERE c."id" = ?', (team_id,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None

def get_all() -> list[Team]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(_SELECT + ' ORDER BY t."название", c."название_команды"')
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]

def get_by_tournament(tournament_id: int) -> list[Team]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        _SELECT + ' WHERE c."турнир_id" = ? ORDER BY c."название_команды"',
        (tournament_id,),
    )
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]

def count_by_tournament(tournament_id: int) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT COUNT(*) FROM "команды" WHERE "турнир_id" = ?', (tournament_id,)
    )
    count = cur.fetchone()[0]
    conn.close()
    return count

def update(team_id: int, name: str, tournament_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        '''UPDATE "команды"
           SET "название_команды" = ?, "турнир_id" = ?
           WHERE "id" = ?''',
        (name, tournament_id, team_id),
    )
    conn.commit()
    conn.close()

def delete(team_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM "команды" WHERE "id" = ?', (team_id,))
    conn.commit()
    conn.close()