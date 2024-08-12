import logging
import traceback
from http import HTTPStatus

from flask import Blueprint

from DTOs.exception_dto import ExceptionDTO
from exceptions.exceptions import BadRequestException

error_handler_bp = Blueprint('error_handler', __name__)


@error_handler_bp.app_errorhandler(Exception)
def general_exception(e: Exception):
    logging.error(f'Internal server error. Exception type: {type(e)}. Exception message: {str(e)}')
    logging.error(traceback.format_exc())
    return ExceptionDTO(HTTPStatus.INTERNAL_SERVER_ERROR.value, 'Internal Server Error').to_dict(), HTTPStatus.INTERNAL_SERVER_ERROR.value


@error_handler_bp.app_errorhandler(BadRequestException)
def bad_request_exception(e: BadRequestException):
    logging.error(f'Bad Request. Exception type: {type(e)}. Exception message: {str(e)}')
    return ExceptionDTO(HTTPStatus.BAD_REQUEST.value, 'Bad Request', str(e)).to_dict(), HTTPStatus.BAD_REQUEST.value
