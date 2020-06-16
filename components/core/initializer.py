import sys
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from gevent import monkey

from utils.app_constants import SERVER_SECRET_KEY

monkey.patch_all(ssl=False)

server = Flask(__name__)
server.config['SECRET_KEY'] = SERVER_SECRET_KEY
socketio = SocketIO(server, cors_allowed_origins="*", debug=True, logger=True, engineio_logger=True, ping_timeout=600)
cors = CORS(server)
p = None
verbose = False

if len(sys.argv) == 2 and sys.argv[1] == '-v':
	verbose = True
