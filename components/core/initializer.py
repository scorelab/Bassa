import sys
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from gevent import monkey

from utils.app_constants import server_secret_key

monkey.patch_all(ssl=False)

server = Flask(__name__)
server.config['SECRET_KEY'] = server_secret_key
socketio = SocketIO(server, debug=True, logger=True, engineio_logger=True, ping_timeout=600)
cors = CORS(server)
p = None
verbose = False

if len(sys.argv) == 2 and sys.argv[1] == '-v':
	verbose = True