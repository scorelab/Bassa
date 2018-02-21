import json
import urllib.error
import urllib.parse
import urllib.request
from multiprocessing import Process
from Auth import *
from DownloadDaemon import starter
from DownloadManager import *
from flask import Flask, Blueprint
from flask import request, Response, g
from flask import send_file
from flask.ext.cors import CORS
from flask_socketio import SocketIO
from gevent import monkey
import logging

monkey.patch_all(ssl=False)

server = Flask(__name__)
server.config['SECRET_KEY'] = "123456789"
download_blueprint = Blueprint('download_blueprint', __name__)
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


@download_blueprint.route('/download/start')
def start():
    try:
        token = request.headers['key']
        if str(token) != server.config['SECRET_KEY']:
            return "{'error':'not authorized'}", 403
        global p
        p = Process(target=starter, args=(socketio,))
        p.start()
        return '{"status":"' + str(p.pid) + '"}'
    except Exception as e:
        return '{"error":"' + e.message + '"}', 400


@download_blueprint.route('/download/kill')
def kill():
    try:
        token = request.headers['key']
        if str(token) != server.config['SECRET_KEY']:
            return "{'error':'not authorized'}", 403
        if p is not None:
            p.terminate()
            p.join()
            jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 'qwer', 'method': 'aria2.pauseAll'})
            jsonreq = jsonreq.encode('ascii')
            req = urllib.request.Request('http://localhost:6800/jsonrpc', jsonreq)
            if verbose:
                with urllib.request.urlopen(req) as response:
                    logging.debug(response.read())
        if not p.is_alive():
            return '{"status":"success"}'
        else:
            return '{"error":"error"}'
    except Exception as e:
        return '{"error":"' + e.message + '"}', 400


@download_blueprint.route('/api/download', methods=['POST'])
def add_download_request():
    token = token_validator(request.headers['token'])
    if token is not None:
        data = request.get_json(force=True)
        try:
            if check_if_bandwidth_exceeded(g.user.userName):
                resp = Response(response='{"quota":"exceeded"}', status=400)
            else:
                new_download = Download(data['link'], g.user.userName)
                status = add_download(new_download)
                if status == "success":
                    resp = Response(response='{"status":"' + status + '"}', status=200)
                else:
                    resp = Response(response='{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response(response='{"error":"' + e.message + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


@download_blueprint.route('/api/download/<_id>', methods=['DELETE'])
def remove_download_request(_id):
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = remove_download(_id, g.user.userName)
            if status == "success":
                resp = Response(response='{"status":"' + status + '"}', status=200)
            else:
                resp = Response(response='{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response(response='{"error":"' + e.message + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


@download_blueprint.route('/api/download/rate/<_id>', methods=['POST'])
def rate_download_request(_id):
    token = token_validator(request.headers['token'])
    if token is not None:
        data = request.get_json(force=True)
        try:
            status = rate_download(_id, g.user.userName, data['rate'])
            if status == "success":
                resp = Response(response='{"status":"' + status + '"}', status=200)
            else:
                resp = Response(response='{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response(response='{"error":"' + e.message + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


@download_blueprint.route('/api/user/downloads/<int:limit>', methods=['GET'])
def get_downloads_user_request(limit):
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = get_downloads_user(g.user.userName, int(limit))
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response(response='{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response(response='{"error":"' + e.message + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


@download_blueprint.route('/api/downloads/<int:limit>', methods=['GET'])
def get_downloads_request(limit):
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = get_downloads(int(limit))
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response(response='{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response(response='{"error":"' + e.message + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


@download_blueprint.route('/api/download/<_id>', methods=['GET'])
def get_download(_id):
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = get_download_path(int(_id))
            if status is not None and status != "db connection error":
                if verbose:
                    logging.debug(status)
                return send_file(status, as_attachment=True, mimetype='multipart/form-data')
            else:
                return '{"error":"file not found"}', 404
        except Exception as e:
            resp = Response(response="{'error':'" + e.message + "'}", status=400)
            return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403