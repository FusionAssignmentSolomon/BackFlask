from enum import Enum


class GameStateEnum(str, Enum):
    X = 'X',
    O = 'O',
    DRAW = 'draw',
    EMPTY = ''
