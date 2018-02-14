import _thread
from flask import Flask, Blueprint
from flask import request, abort, Response, g
from Auth import *
from Models import *
import logging
import json
from EMail import send_mail
import sys

from gevent import monkey

monkey.patch_all(ssl=False)

server = Flask(__name__)
user_blueprint = Blueprint('user_blueprint', __name__)
server.config['SECRET_KEY'] = "123456789"

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


@user_blueprint.route('/api/login', methods=['POST'])
def login():
    user_name = request.form['user_name']
    password = request.form['password']
    if user_login(user_name, password):
        if check_approved(user_name, password):
            user = get_user(user_name)
            token = generate_auth_token(user, server.config['SECRET_KEY'])
            resp = Response(response='{"auth":"' + str(user.auth) + '"}', status=200)
            resp.headers['token'] = token
            resp.headers['Access-Control-Expose-Headers'] = 'token'
            return resp
        else:
            resp = Response(response='{"status": "unapproved"}', status=401)
            return resp
    else:
        abort(403)


@user_blueprint.route('/api/regularuser', methods=['POST'])
def regular_user_request():
    data = request.get_json(force=True)
    try:
        new_user = User(data['user_name'], data['password'], 1, data['email'])
        status = add_regular_user(new_user)
        if status == "success":
            resp = Response(response='{"status": "' + status + '"}', status=200)
            # _thread.start_new_thread(send_mail, (data['email'],"Hi\n Your Bassa account will be axpproved after it
            # has been approved by an admin."))
        else:
            resp = Response(response='{"error":"' + status + '"}', status=400)
    except Exception as e:
        resp = Response(response='{"error":"username exists"}', status=400)
        logging.exception(e)
    return resp


@user_blueprint.route('/api/user', methods=['POST'])
def add_user_request():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        data = request.get_json(force=True)
        try:
            new_user = User(data['user_name'], data['password'], int(data['auth']), data['email'])
            status = add_user(new_user)
            if status == "success":
                resp = Response(response='{"status": "' + status + '"}', status=200)
                _thread.start_new_thread(send_mail, (data['email'], "Hi\n Your user name for Bassa is " + data[
                    'user_name'] + " and your password is " + data['password']))
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


@user_blueprint.route('/api/user/<string:username>', methods=['DELETE'])
def remove_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = remove_user(username)
            if status == "success":
                resp = Response(response='{"status": "' + status + '"}', status=200)
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


@user_blueprint.route('/api/user/<string:username>', methods=['PUT'])
def update_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        data = request.get_json(force=True)
        try:
            new_user = User(data['user_name'], data['password'], int(data['auth']), data['email'])
            status = update_user(new_user, username)
            if status == "success":
                resp = Response(response='{"status": "' + status + '"}', status=200)
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


@user_blueprint.route('/api/user', methods=['GET'])
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


@user_blueprint.route('/api/user/requests', methods=['GET'])
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


@user_blueprint.route('/api/user/approve/<string:username>', methods=['POST'])
def approve_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = approve_user(username)
            if status == "success":
                resp = Response(response='{"status": "' + status + '"}', status=200)
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


@user_blueprint.route('/api/user/blocked', methods=['GET'])
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


@user_blueprint.route('/api/user/blocked/<string:username>', methods=['POST'])
def block_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = block_user(username)
            if status == "success":
                resp = Response(response='{"status": "' + status + '"}', status=200)
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


@user_blueprint.route('/api/user/blocked/<string:username>', methods=['DELETE'])
def unblock_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = unblock_user(username)
            if status == "success":
                resp = Response(response='{"status": "' + status + '"}', status=200)
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


@user_blueprint.route('/api/user/heavy', methods=['GET'])
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
