from flask import Flask
from flask.ext.cors import CORS
from flask import send_file, send_from_directory
from flask import g
from flask_socketio import SocketIO, join_room
from Auth import *
import os
import sys
from Routes.index import user_blueprint
from Routes.index import download_blueprint
from gevent import monkey

monkey.patch_all(ssl=False)

server = Flask(__name__)
server.config['SECRET_KEY'] = "123456789"
server.register_blueprint(user_blueprint)
server.register_blueprint(download_blueprint)
socketio = SocketIO(server, debug=True, logger=True, engineio_logger=True, ping_timeout=600)
cors = CORS(server)
p = None
verbose = False

if len(sys.argv) == 2 and sys.argv[1] == '-v':
    verbose = True


def token_validator(token):
    user = verify_auth_token(token, server.config['SECRET_KEY'])
    if user is not None:
        g.user = user
        token = generate_auth_token(user, server.config['SECRET_KEY'])
        return token
    return None


@server.route('/ui/<string:path>')
def serve_ui(path):
    return send_from_directory(os.path.dirname(os.path.realpath(__file__)) + "/ui", path)


@server.route('/ui/')
def serve_ui1():
    return send_file(os.path.dirname(os.path.realpath(__file__)) + "/ui/index.html")


@socketio.on('join', namespace='/progress')
def on_join(data):
    room = data['room']
    if room != '':
        join_room(room)
