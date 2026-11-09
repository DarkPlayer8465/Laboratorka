# models/player.py
from dataclasses import dataclass

@dataclass
class Player:
    player_id: int
    name: str
    position: str
    team_id: int

    team_name: str | None = None         # служебные поля (из JOIN)
    tournament_name: str | None = None