from dataclasses import dataclass
from typing import Optional

from dataclasses_json import DataClassJsonMixin

from enums.game_state_enum import GameStateEnum
from enums.player_type_enum import PlayerTypeEnum


@dataclass
class MakeMoveDTO(DataClassJsonMixin):
    row: int
    col: int


@dataclass
class UpdateDTO(DataClassJsonMixin):
    board: list[list[str]]
    current_player: GameStateEnum
    winner: Optional[GameStateEnum]


@dataclass
class JoinDTO(DataClassJsonMixin):
    name: str


@dataclass
class JoinResponseDTO(DataClassJsonMixin):
    player_type: PlayerTypeEnum
