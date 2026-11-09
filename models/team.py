# models/team.py
from dataclasses import dataclass

@dataclass
class Team:
    team_id: int
    name: str
    tournament_id: int

    tournament_name: str | None = None   # служебное поле (из JOIN)