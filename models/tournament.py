# models/tournament.py
from dataclasses import dataclass

@dataclass
class Tournament:
    tournament_id: int
    name: str
    sport: str