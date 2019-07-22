from flask import json
from flask import request, Response, g
from utils.token_utils import token_validator
from utils.entity_utils import entity_type


def fetch_entity_children(id):
    token = request.headers.get('token')
    if token is None:
        return '{"error":"token error"}', 403
    try:
        entity = entity_type('fr')
        fetch_response = entity.get_all(id)
        if not isinstance(fetch_response, str):
            return Response(response=json.dumps(fetch_response), status=200)
        else:
            resp = Response('{"error":"' + fetch_response + '"}', status=500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def fetch_entity(id):
    token = request.headers.get('token')
    if token is None:
        return '{"error":"token error"}', 403
    try:
        type = request.args.get('type')
        if not type == 'fr' or type =='fl':
            return Response('{"error":"invalid parameter"}', status=400)

        entity = entity_type(type)
        fetch_response = entity.get(id)
        if not isinstance(fetch_response, str):
            resp = Response(response=json.dumps(fetch_response), status=200)
        else:
            resp = Response('{"error":"' + fetch_response + '"}', status=500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def add_entity(user_id):
    token = request.headers.get('token')
    if token is None:
        return '{"error":"token error"}', 403
    data = request.get_json(force=True)
    try:
        type = request.args.get('type')
        if not type == 'fr' or type =='fl':
            return Response('{"error":"invalid parameter"}', status=400)

        name = data['name']
        parent_id = data['parent_id']
        entity = entity_type(type)

        add_response = entity.create(name, user_id, parent_id)
        resp = Response(response='{"status":"' + add_response + '"}',
                    status=200 if add_response == "success" else 500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def edit_entity(id):
    token = request.headers.get('token')
    if token is None:
        return '{"error":"token error"}', 403
    data = request.get_json(force=True)
    try:
        type = request.args.get('type')
        if not type == 'fr' or type =='fl':
            return Response('{"error":"invalid parameter"}', status=400)

        name = data['name']
        entity = entity_type(type)

        edit_response = entity.update(name, id)
        resp = Response(response='{"status":"' + edit_response + '"}',
                    status=200 if edit_response == "success" else 500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def remove_entity(id):
    token = request.headers.get('token')
    if token is None:
        return '{"error":"token error"}', 403
    try:
        type = request.args.get('type')
        if not type == 'fr' or type =='fl':
            return Response('{"error":"invalid parameter"}', status=400)

        entity = entity_type(type)
        delete_response = entity.delete(id)
        resp = Response(response='{"status":"' + delete_response + '"}',
                    status=200 if delete_response == "success" else 500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def move_entity(id):
    token = request.headers.get('token')
    if token is None:
        return '{"error":"token error"}', 403
    data = request.get_json(force=True)
    try:
        type = request.args.get('type')
        if not type == 'fr' or type =='fl':
            return Response('{"error":"invalid parameter"}', status=400)

        name = data['parent_name']
        entity = entity_type(type)

        move_response = entity.move(id, name)
        resp = Response(response='{"status":"' + move_response + '"}',
                    status=200 if move_response == "success" else 500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp
