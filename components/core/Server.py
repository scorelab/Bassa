from flask import Flask
from flask.ext.cors import CORS
from flask import send_file, send_from_directory
from flask import request, jsonify, abort, Response, g
from flask_socketio import SocketIO, join_room
from Auth import *
from Models import *
from DownloadManager import *
import json, urllib.request, urllib.error, urllib.parse, os, _thread
from multiprocessing import Process
from DownloadDaemon import starter
from EMail import send_mail
import sys
from gevent import monkey

monkey.patch_all(ssl=False)

server = Flask(__name__)
server.config['SECRET_KEY'] = "123456789"
socketio = SocketIO(server, debug=True, logger=True, engineio_logger=True, ping_timeout=600)
cors = CORS(server)
p = None
verbose = False

if len(sys.argv) == 2 and sys.argv[1] == '-v':
    verbose = True

def token_validator(token):
    user = verify_auth_token(token, server.config['SECRET_KEY'])
    if user != None:
        g.user = user
        token = generate_auth_token(user, server.config['SECRET_KEY'])
        return token
    return None


@server.route('/ui/<string:path>')
def serve_ui(path):
    return send_from_directory(os.path.dirname(os.path.realpath(__file__))+"/ui", path)

@server.route('/ui/')
def serve_ui1():
    return send_file(os.path.dirname(os.path.realpath(__file__))+"/ui/index.html")

# Import routes
from routes import *
from file_sender import sender

# register endpoints
server.add_url_rule('/api/get/file', 'send_file_from_path', sender.send_file_from_path, methods=['GET'])
