from flask import Blueprint, request
from flask_socketio import emit

from DTOs.play_dto import *
from entities.player import Player
from enums.websocket_state_enum import WebSocketStateEnum
from exceptions.exceptions import BadRequestException
from shared_game_manager import game_manager
from shared_socketio import socketio

game_bp = Blueprint('game_api', __name__)


@socketio.on(WebSocketStateEnum.MAKE_MOVE)
def handle_make_move(data):
    try:
        print(data)
        make_move_dto = MakeMoveDTO.from_dict(data)
        validate(make_move_dto.row, make_move_dto.col)
        game_manager.play_turn(make_move_dto.row, make_move_dto.col)
        emit(WebSocketStateEnum.UPDATE, UpdateDTO(
            board=game_manager.board,
            current_player=game_manager.current_player,
            winner=game_manager.winner
        ).to_dict(), broadcast=True)
        if game_manager.winner:
            game_manager.clear_board()

    except Exception as e:
        print({'message': str(e)})
        emit(WebSocketStateEnum.ERROR, {'message': str(e)})


@socketio.on(WebSocketStateEnum.JOIN)
def handle_connect(data):
    print('Client connected')
    join_dto = JoinDTO.from_dict(data)
    player: Player = game_manager.set_player(join_dto.name)
    emit(WebSocketStateEnum.JOIN_RESPONSE, JoinResponseDTO(
        player_type=player.type
    ).to_dict())

# @socketio.on('disconnect')
# def handle_disconnect():
#     print('Client disconnected')

@socketio.on(WebSocketStateEnum.ERROR)
def handle_error(data):
    print(f"Error: {data.get('message')}")


def validate(row: int, col: int) -> None:
    if not game_manager.validate_play(row, col):
        raise BadRequestException('Got invalid values - check ROW, COL or maybe the square is already taken')