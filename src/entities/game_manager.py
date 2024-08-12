from dataclasses import dataclass, field
from typing import Optional

from entities.player import Player
from enums.game_state_enum import GameStateEnum
from enums.player_type_enum import PlayerTypeEnum
from exceptions.exceptions import *


@dataclass
class GameManager:
    board: list[list[str]] = field(default_factory=lambda: [['' for _ in range(3)] for _ in range(3)])
    current_player: GameStateEnum = GameStateEnum.X
    winner: Optional[GameStateEnum] = None
    player_a: Optional[Player] = None
    player_b: Optional[Player] = None

    def play_turn(self, row: int, col: int) -> None:
        if not self.validate_play(row, col):
            raise BadRequestException('Invalid values for ROW or COL or square is taken')
        if self.winner:
            raise GameFinishedException('There is a winner')
        self.board[row][col] = self.current_player
        if self.check_for_winner():
            self.winner = self.current_player
        elif self.check_for_draw():
            self.winner = GameStateEnum.DRAW
        else:
            self.change_current_player()

    def check_for_winner(self) -> bool:
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False

    def check_for_draw(self) -> bool:
        # If all the squares are filled but no winner it is a draw
        return all(self.board[row][col] != '' for row in range(3) for col in range(3)) and self.winner is None

    def change_current_player(self) -> None:
        self.current_player = GameStateEnum.X if self.current_player == GameStateEnum.O else GameStateEnum.O

    def validate_play(self, row: int, col: int) -> bool:
        if (row < 0 or row > 3) or (col < 0 or col > 3):
            return False
        if self.board[row][col] is not '':
            return False
        return True

    def set_player(self, player_name: str) -> Player:
        if self.player_a is None:
            self.player_a = Player(player_name, PlayerTypeEnum.X)
            return self.player_a
        else:
            self.player_b = Player(player_name, PlayerTypeEnum.O)
            return self.player_b

    def clear_board(self) -> None:
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.current_player = GameStateEnum.X
