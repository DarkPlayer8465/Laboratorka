# services/player_service.py
from repositories import player_repository, team_repository

def get_all_players():
    return player_repository.get_all()

def get_players_by_team(team_id: int):
    if not team_repository.get_by_id(team_id):
        raise Exception("Команда не найдена")
    return player_repository.get_by_team(team_id)

def _validate(name: str, position: str, team_id: int):
    if not name.strip():
        raise Exception("Имя игрока не может быть пустым")
    if not position.strip():
        raise Exception("Позиция не может быть пустой")
    if not team_repository.get_by_id(team_id):
        raise Exception("Команда не найдена")

def _check_duplicate(name: str, team_id: int, exclude_id: int | None = None):
    for p in player_repository.get_by_team(team_id):
        if p.player_id != exclude_id and p.name.lower() == name.strip().lower():
            raise Exception("Игрок с таким именем уже есть в этой команде")

def create_player(name: str, position: str, team_id: int):
    _validate(name, position, team_id)
    _check_duplicate(name, team_id)
    player_repository.create(name.strip(), position.strip(), team_id)

def update_player(player_id: int, name: str, position: str, team_id: int):
    if not player_repository.get_by_id(player_id):
        raise Exception("Игрок не найден")
    _validate(name, position, team_id)
    _check_duplicate(name, team_id, exclude_id=player_id)
    player_repository.update(player_id, name.strip(), position.strip(), team_id)

def delete_player(player_id: int):
    if not player_repository.get_by_id(player_id):
        raise Exception("Игрок не найден")
    player_repository.delete(player_id)