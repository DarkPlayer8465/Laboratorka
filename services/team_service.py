# services/team_service.py
from repositories import team_repository, tournament_repository, player_repository

def get_all_teams():
    return team_repository.get_all()

def get_teams_by_tournament(tournament_id: int):
    if not tournament_repository.get_by_id(tournament_id):
        raise Exception("Турнир не найден")
    return team_repository.get_by_tournament(tournament_id)

def _validate(name: str, tournament_id: int):
    if not name.strip():
        raise Exception("Название команды не может быть пустым")
    if not tournament_repository.get_by_id(tournament_id):
        raise Exception("Турнир не найден")

def _check_duplicate(name: str, tournament_id: int, exclude_id: int | None = None):
    # название должно быть уникальным в пределах одного турнира
    for t in team_repository.get_by_tournament(tournament_id):
        if t.team_id != exclude_id and t.name.lower() == name.strip().lower():
            raise Exception("Команда с таким названием уже есть в этом турнире")

def create_team(name: str, tournament_id: int):
    _validate(name, tournament_id)
    _check_duplicate(name, tournament_id)
    team_repository.create(name.strip(), tournament_id)

def update_team(team_id: int, name: str, tournament_id: int):
    if not team_repository.get_by_id(team_id):
        raise Exception("Команда не найдена")
    _validate(name, tournament_id)
    _check_duplicate(name, tournament_id, exclude_id=team_id)
    team_repository.update(team_id, name.strip(), tournament_id)

def delete_team(team_id: int):
    if not team_repository.get_by_id(team_id):
        raise Exception("Команда не найдена")
    if player_repository.count_by_team(team_id) > 0:
        raise Exception("Нельзя удалить команду, в составе которой есть игроки")
    team_repository.delete(team_id)