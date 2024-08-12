from dataclasses import dataclass
from typing import Optional
from enums.player_type_enum import PlayerTypeEnum


@dataclass
class Player:
    name: str
    type: Optional[PlayerTypeEnum] = None