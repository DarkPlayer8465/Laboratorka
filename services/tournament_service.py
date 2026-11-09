# services/tournament_service.py
from repositories import tournament_repository, team_repository

def get_all_tournaments():
    return tournament_repository.get_all()

def _validate(name: str, sport: str):
    if not name.strip():
        raise Exception("Название турнира не может быть пустым")
    if not sport.strip():
        raise Exception("Вид спорта не может быть пустым")

def _check_duplicate(name: str, sport: str, exclude_id: int | None = None):
    for t in tournament_repository.get_all():
        if (
            t.tournament_id != exclude_id
            and t.name.lower() == name.strip().lower()
            and t.sport.lower() == sport.strip().lower()
        ):
            raise Exception("Такой турнир уже существует")

def create_tournament(name: str, sport: str):
    _validate(name, sport)
    _check_duplicate(name, sport)
    tournament_repository.create(name.strip(), sport.strip())

def update_tournament(tournament_id: int, name: str, sport: str):
    if not tournament_repository.get_by_id(tournament_id):
        raise Exception("Турнир не найден")
    _validate(name, sport)
    _check_duplicate(name, sport, exclude_id=tournament_id)
    tournament_repository.update(tournament_id, name.strip(), sport.strip())

def delete_tournament(tournament_id: int):
    if not tournament_repository.get_by_id(tournament_id):
        raise Exception("Турнир не найден")
    if team_repository.count_by_tournament(tournament_id) > 0:
        raise Exception("Нельзя удалить турнир, в котором есть команды")
    tournament_repository.delete(tournament_id)