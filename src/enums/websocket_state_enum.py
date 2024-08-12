from enum import Enum


class WebSocketStateEnum(str, Enum):
    JOIN_RESPONSE = 'JOIN_RESPONSE'
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    ERROR = 'ERROR'
    MAKE_MOVE = 'MAKE_MOVE'
    UPDATE = 'UPDATE'
    JOIN = 'JOIN'
