from flask import Flask
from flask import request, jsonify, abort, Response, g
from redis import Redis
from rq import Queue
from func import downloadMe
from Auth import *
from Models import AuthLeval
import json

server = Flask(__name__)
redis_conn = Redis()
qu = Queue(connection=redis_conn)
server.config['SECRET_KEY'] = "123456789"


def token_validator(token):
    user = verify_auth_token(token, server.config['SECRET_KEY'])
    if user != None:
        g.user = user
        token = generate_auth_token(user, server.config['SECRET_KEY'])
        return token
    return None


@server.route('/')
def index():
    return "Bassa 2"


@server.route('/api/download', methods=['GET'])
def download():
    link = request.args.get('link', '')
    job = qu.enqueue(downloadMe, link)
    return '{ "msg": "Added to the queue"}'


@server.route('/api/login', methods=['POST'])
def login():
    userName = request.form['user_name']
    password = request.form['password']
    if user_login(userName, password):
        user = get_user(userName)
        token = generate_auth_token(user, server.config['SECRET_KEY'])
        resp = Response(status=200)
        resp.headers['token'] = token
        return resp
    else:
        abort(403)


@server.route('/api/user', methods=['POST'])
def add_user_request():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        data = request.get_json(force=True)
        try:
            newUser = User(data['user_name'], data['password'], int(data['auth']), data['email'])
            status = add_user(newUser)
            if status == "success":
                resp = Response(response="{'status':'" + status + "'}", status=200)
            else:
                resp = Response(response="{'error':'" + status + "'}", status=400)
        except Exception, e:
            resp = Response(response="{'error':'" + e.message + "'}", status=400)
        resp.headers['token'] = token
        return resp
    elif token is not None:
        return "{'error':'not authorized'}", 403
    else:
        return "{'error':'token error'}", 403


@server.route('/api/user/<string:username>', methods=['DELETE'])
def remove_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = remove_user(username)
            if status == "success":
                resp = Response(response="{'status':'" + status + "'}", status=200)
            else:
                resp = Response(response="{'error':'" + status + "'}", status=400)
        except Exception, e:
            resp = Response(response="{'error':'" + e.message + "'}", status=400)
        resp.headers['token'] = token
        return resp
    elif token is not None:
        return "{'error':'not authorized'}", 403
    else:
        return "{'error':'token error'}", 403


@server.route('/api/user/<string:username>', methods=['PUT'])
def update_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        data = request.get_json(force=True)
        try:
            newUser = User(data['user_name'], data['password'], int(data['auth']), data['email'])
            status = update_user(newUser, username)
            if status == "success":
                resp = Response(response="{'status':'" + status + "'}", status=200)
            else:
                resp = Response(response="{'error':'" + status + "'}", status=400)
        except Exception, e:
            resp = Response(response="{'error':'" + e.message + "'}", status=400)
        resp.headers['token'] = token
        return resp
    elif token is not None:
        return "{'error':'not authorized'}", 403
    else:
        return "{'error':'token error'}", 403


@server.route('/api/user', methods=['GET'])
def get_users_request():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = get_users()
            if not isinstance(status, basestring):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response(response="{'error':'" + status + "'}", status=400)
        except Exception, e:
            resp = Response(response="{'error':'" + e.message + "'}", status=400)
        resp.headers['token'] = token
        return resp
    elif token is not None:
        return "{'error':'not authorized'}", 403
    else:
        return "{'error':'token error'}", 403


@server.route('/api/user/blocked', methods=['GET'])
def get_blocked_users_request():
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = get_blocked_users()
            if not isinstance(status, basestring):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response(response="{'error':'" + status + "'}", status=400)
        except Exception, e:
            resp = Response(response="{'error':'" + e.message + "'}", status=400)
        resp.headers['token'] = token
        return resp
    elif token is not None:
        return "{'error':'not authorized'}", 403
    else:
        return "{'error':'token error'}", 403

server.route('/api/user/blocked/<string:username>', methods=['POST'])
def block_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = block_user(username)
            if status == "success":
                resp = Response(response="{'status':'" + status + "'}", status=200)
            else:
                resp = Response(response="{'error':'" + status + "'}", status=400)
        except Exception, e:
            resp = Response(response="{'error':'" + e.message + "'}", status=400)
        resp.headers['token'] = token
        return resp
    elif token is not None:
        return "{'error':'not authorized'}", 403
    else:
        return "{'error':'token error'}", 403

server.route('/api/user/blocked/<string:username>', methods=['DELETE'])
def unblock_user_request(username):
    token = token_validator(request.headers['token'])
    if token is not None and g.user.auth == AuthLeval.ADMIN:
        try:
            status = unblock_user(username)
            if status == "success":
                resp = Response(response="{'status':'" + status + "'}", status=200)
            else:
                resp = Response(response="{'error':'" + status + "'}", status=400)
        except Exception, e:
            resp = Response(response="{'error':'" + e.message + "'}", status=400)
        resp.headers['token'] = token
        return resp
    elif token is not None:
        return "{'error':'not authorized'}", 403
    else:
        return "{'error':'token error'}", 403