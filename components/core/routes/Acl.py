from flask import json
from flask import request, abort, Response, g
from AclManager import *


def check_access(id, user_id):
    token = token_validator(request.headers['token'])
    if token is None:
        return '{"error":"token error"}', 403
    try:
        entity = request.args.get('type')
        check_response = get_access(id, user_id, entity)
        if not isinstance(check_response, str):
            resp = Response(response=json.dumps(check_response), status=200)
        else:
            resp = Response('{"error":"' + check_response + '"}', status=400)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def grant_access(id):
    token = token_validator(request.headers['token'])
    if token is None:
        return '{"error":"token error"}', 403
    data = request.get_json(force=True)
    try:
        entity = request.args.get('type')
        user_name = data['user_name']
        access = data['access']

        grant_response = give_access(id, user_name, entity, access)
        resp = Response(response='{"status":"' + grant_response + '"}',
                    status=200 if grant_response == "success" else 400)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp