import sys, os
dir_path = os.path.abspath(__file__)[:-15]
sys.path.append(dir_path)

from flask import Flask
from flask.ext.cors import CORS
from flask import send_file, send_from_directory
from flask import request, jsonify, abort, Response, g
from flask_socketio import SocketIO, join_room
from Auth import *
from Models import *
from DownloadManager import *
import urllib.request, urllib.error, urllib.parse, _thread
from gevent import monkey


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
            # _thread.start_new_thread(send_mail, (data['email'],"Hi\n Your Bassa account will be activated after it has been approved by an admin."))
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
            resp = Response(response='{"status":"'+ status + '"}', status= (200 if status == "success" else 400))
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
            resp = Response(response='{"status":"'+ status + '"}', status= (200 if status == "success" else 400))
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
            resp = Response(response=((json.dumps(status),status=200) if not isinstance(status, str) else ('{"error":"' + status + '"}', status=400)))
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
            resp = Response(response=((json.dumps(status),status=200) if not isinstance(status, str) else ('{"error":"' + status + '"}', status=400)))
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
            resp = Response(response='{"status":"'+ status + '"}', status= (200 if status == "success" else 400))
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
            resp = Response(response=((json.dumps(status),status=200) if not isinstance(status, str) else ('{"error":"' + status + '"}', status=400)))
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
            resp = Response(response='{"status":"'+ status + '"}', status= (200 if status == "success" else 400))
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
            resp = Response(response='{"status":"'+ status + '"}', status= (200 if status == "success" else 400))
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
            resp = Response(response=((json.dumps(status),status=200) if not isinstance(status, str) else ('{"error":"' + status + '"}', status=400)))
        except Exception as e:
            resp = Response(response='{"error":"' + e.message + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
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
            resp = Response(response=((json.dumps(status),status=200) if not isinstance(status, str) else ('{"error":"' + status + '"}', status=400)))
        except Exception as e:
            resp = Response(response='{"error":"' + e.message + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403

