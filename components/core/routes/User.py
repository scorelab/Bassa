from flask import json
from flask import request, abort, Response, g
from Auth import *
from EMail import send_mail
from Models import *
from DownloadManager import *
import _thread
from utils.token_utils import token_validator
from utils.app_constants import SERVER_SECRET_KEY


def login():
    userName = request.form['user_name']
    password = request.form['password']
    if user_login(userName, password):
        if check_approved(userName, password):
            user = get_user(userName)
            token = generate_auth_token(user, SERVER_SECRET_KEY)
            resp = Response(response='{"auth":"'+ str(user.auth) + '"}',status=200)
            resp.headers['token'] = token
            resp.headers['Access-Control-Expose-Headers'] = 'token'
            return resp
        else:
            resp = Response(response='{"status": "unapproved"}',status=401)
            return resp
    else:
        abort(403)


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
        resp = Response(response='{"error":"Connection error"}', status=500)
    return resp


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
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


def remove_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = remove_user(username)
            resp = Response(response='{"status":"'+ status + '"}', status= (200 if status == "success" else 400))
        except Exception as e:
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


def update_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        data = request.get_json(force=True)
        try:
            newUser = User(data['user_name'], data['password'], int(data['auth']), data['email'])
            status = update_user(newUser, username)
            resp = Response(response='{"status":"'+ status + '"}', status= (200 if status == "success" else 400))
        except Exception as e:
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


def get_users_request():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = get_users()
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status),status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


def get_user_signup_requests():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = get_signup_requests()
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status),status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


def approve_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = approve_user(username)
            resp = Response(response='{"status":"'+ status + '"}', status= (200 if status == "success" else 400))
        except Exception as e:
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


def get_blocked_users_request():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = get_blocked_users()
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status),status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


def block_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = block_user(username)
            resp = Response(response='{"status":"'+ status + '"}', status= (200 if status == "success" else 400))
        except Exception as e:
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


def unblock_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = unblock_user(username)
            resp = Response(response='{"status":"'+ status + '"}', status= (200 if status == "success" else 400))
        except Exception as e:
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


def get_downloads_user_request(limit):
    token = token_validator(request.headers['token'])
    if token is not None :
        try:
            status = get_downloads_user(g.user.userName, int(limit))
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status),status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403


def get_topten_heaviest_users():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = get_heavy_users()
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status),status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response(response='{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403

