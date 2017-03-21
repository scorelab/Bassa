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

@server.route('/download/start')
def start():
    try:
        token = request.headers['key']
        if str(token)!=server.config['SECRET_KEY']:
            return "{'error':'not authorized'}", 403
        global p
        p = Process(target=starter, args=(socketio,))
        p.start()
        return '{"status":"' + str(p.pid) + '"}'
    except Exception as e:
            return '{"error":"' + e.message + '"}',400

@socketio.on('join', namespace='/progress')
def on_join(data):
    room = data['room']
    if room != '':
        join_room(room)

@server.route('/download/kill')
def kill():
    try:
        token = request.headers['key']
        if str(token)!=server.config['SECRET_KEY']:
            return "{'error':'not authorized'}", 403
        if p is not None:
            p.terminate()
            p.join()
            jsonreq = json.dumps({'jsonrpc':'2.0', 'id':'qwer', 'method':'aria2.pauseAll'})
            jsonreq = jsonreq.encode('ascii')
            c = urllib.request.urlopen('http://localhost:6800/jsonrpc', jsonreq)
            if verbose:
                print(c)
        if not p.is_alive():
            return '{"status":"success"}'
        else:
            return '{"error":"error"}'
    except Exception as e:
        return '{"error":"' + e.message + '"}',400


@server.route('/api/login', methods=['POST'])
def login():
    userName = request.form['user_name']
    password = request.form['password']
    if user_login(userName, password):
        if check_approved(userName, password):
            user = get_user(userName)
            token = generate_auth_token(user, server.config['SECRET_KEY'])
            resp = Response(response='{"auth":"'+ str(user.auth) + '"}',status=200)
            resp.headers['token'] = token
            resp.headers['Access-Control-Expose-Headers'] = 'token'
            return resp
        else:
            resp = Response(response='{"status": "unapproved"}',status=401)
            return resp
    else:
        abort(403)


@server.route('/api/regularuser', methods=['POST'])
def regular_user_request():
    data = request.get_json(force=True)
    try:
        newUser = User(data['user_name'], data['password'], 1, data['email'])
        status = add_regular_user(newUser)
        if status == "success":
            resp = Response(response='{"status": "'+ status + '"}', status=200)
            # _thread.start_new_thread(send_mail, (data['email'],"Hi\n Your Bassa account will be approved after it has been approved by an admin."))
        else:
            resp = Response(response='{"error":"' + status + '"}', status=400)
    except Exception as e:
        resp = Response(response='{"error":"username exists"}', status=400)
    return resp


@server.route('/api/user', methods=['POST'])
def add_user_request():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        data = request.get_json(force=True)
        try:
            newUser = User(data['user_name'], data['password'], int(data['auth']), data['email'])
            status = add_user(newUser)
            if status == "success":
                resp = Response(response='{"status": "'+ status + '"}', status=200)
                _thread.start_new_thread(send_mail, (data['email'],"Hi\n Your user name for Bassa is "+data['user_name']+" and your password is "+ data['password']))
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


@server.route('/api/user/<string:username>', methods=['DELETE'])
def remove_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = remove_user(username)
            if status == "success":
                resp = Response(response='{"status": "'+ status + '"}', status=200)
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


@server.route('/api/user/<string:username>', methods=['PUT'])
def update_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        data = request.get_json(force=True)
        try:
            newUser = User(data['user_name'], data['password'], int(data['auth']), data['email'])
            status = update_user(newUser, username)
            if status == "success":
                resp = Response(response='{"status": "'+ status + '"}', status=200)
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


@server.route('/api/user', methods=['GET'])
def get_users_request():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = get_users()
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

@server.route('/api/user/requests', methods=['GET'])
def get_user_signup_requests():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = get_signup_requests()
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

@server.route('/api/user/approve/<string:username>', methods=['POST'])
def approve_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = approve_user(username)
            if status == "success":
                resp = Response(response='{"status": "'+ status + '"}', status=200)
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

@server.route('/api/user/blocked', methods=['GET'])
def get_blocked_users_request():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = get_blocked_users()
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


@server.route('/api/user/blocked/<string:username>', methods=['POST'])
def block_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = block_user(username)
            if status == "success":
                resp = Response(response='{"status": "'+ status + '"}', status=200)
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


@server.route('/api/user/blocked/<string:username>', methods=['DELETE'])
def unblock_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = unblock_user(username)
            if status == "success":
                resp = Response(response='{"status": "'+ status + '"}', status=200)
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


@server.route('/api/download', methods=['POST'])
def add_download_request():
    token = token_validator(request.headers['token'])
    if token is not None:
        data = request.get_json(force=True)
        try:
            if check_if_bandwidth_exceeded(g.user.userName):
                resp = Response(response='{"quota":"exceeded"}', status=400)
            else:
                newDownload = Download(data['link'], g.user.userName)
                status = add_download(newDownload)
                if status == "success":
                    resp = Response(response='{"status":"'+ status + '"}', status=200)
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


@server.route('/api/download/<int:id>', methods=['DELETE'])
def remove_download_request(id):
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = remove_download(id, g.user.userName)
            if status == "success":
                resp = Response(response='{"status":"'+ status + '"}', status=200)
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


@server.route('/api/download/rate/<int:id>', methods=['POST'])
def rate_download_request(id):
    token = token_validator(request.headers['token'])
    if token is not None:
        data = request.get_json(force=True)
        try:
            status = rate_download(id, g.user.userName, data['rate'])
            if status == "success":
                resp = Response(response='{"status":"'+ status + '"}', status=200)
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


@server.route('/api/user/downloads/<int:limit>', methods=['GET'])
def get_downloads_user_request(limit):
    token = token_validator(request.headers['token'])
    if token is not None :
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


@server.route('/api/downloads/<int:limit>', methods=['GET'])
def get_downloads_request(limit):
    token = token_validator(request.headers['token'])
    if token is not None :
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

@server.route('/api/download/<int:id>', methods=['GET'])
def get_download(id):
    token = token_validator(request.headers['token'])
    if token is not None :
        try:
            status = get_download_path(int(id))
            if status is not None and status!="db connection error":
                if verbose:
                    print(status)
                return send_file(status,as_attachment=True, mimetype='multipart/form-data')
            else:
                return '{"error":"file not found"}', 404
        except Exception as e:
            resp = Response(response="{'error':'" + e.message + "'}", status=400)
            return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403

@server.route('/api/user/heavy', methods=['GET'])
def get_topten_heaviest_users():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = get_heavy_users()
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
