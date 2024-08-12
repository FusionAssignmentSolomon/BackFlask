import logging

from flask import Flask

from exceptions.exceptions_config import error_handler_bp
from routers.game_api import game_bp
from shared_game_manager import game_manager
from shared_socketio import socketio

# from routers.join_api import join_bp

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
socketio.init_app(app, cors_allowed_origins="http://localhost:3000")

# app.register_blueprint(error_handler_bp)
# app.register_blueprint(join_bp)
app.register_blueprint(game_bp)


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    logging.info('Starting server')
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
