from flask import json
from flask import request, Response, g
from utils.token_utils import token_validator
from utils.entity_utils import entity_type


def fetch_entity_children(id, user_id):
    token = token_validator(request.headers.get('token'))
    if token is None:
        return '{"error":"token error"}', 403
    try:
        entity = entity_type('fr')

        fetch_response = entity.get_all(user_id, id)
        if not isinstance(fetch_response, str):
            return Response(response=json.dumps(fetch_response), status=200)
        else:
            resp = Response('{"error":"' + fetch_response + '"}', status=500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def fetch_entity(id, user_id):
    token = token_validator(request.headers.get('token'))
    if token is None:
        return '{"error":"token error"}', 403
    try:
        e_type = request.args.get('type')
        if not e_type == 'fr' and not e_type =='fl':
            return Response('{"error":"invalid parameter"}', status=400)
        entity = entity_type(e_type)

        fetch_response = entity.get(id, user_id)
        if not isinstance(fetch_response, str):
            resp = Response(response=json.dumps(fetch_response), status=200)
        else:
            resp = Response('{"error":"' + fetch_response + '"}', status=500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def add_entity(id, user_id):
    token = token_validator(request.headers.get('token'))
    if token is None:
        return '{"error":"token error"}', 403
    try:
        e_type = request.args.get('type')
        if not e_type == 'fr':
            return Response('{"error":"invalid parameter"}', status=400)

        name = request.form['name']
        entity = entity_type(e_type)

        add_response = entity.create(name, user_id, id)
        resp = Response(response='{"status":"' + add_response + '"}',
                    status=200 if add_response == "success" else 500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def edit_entity(id, user_id):
    token = token_validator(request.headers.get('token'))
    if token is None:
        return '{"error":"token error"}', 403
    try:
        e_type = request.args.get('type')
        if not e_type == 'fr' and not e_type =='fl':
            return Response('{"error":"invalid parameter"}', status=400)

        new_name = request.form['new_name']
        entity = entity_type(e_type)

        edit_response = entity.update(new_name, id, user_id)
        resp = Response(response='{"status":"' + edit_response + '"}',
                    status=200 if edit_response == "success" else 500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def remove_entity(id, user_id):
    token = token_validator(request.headers.get('token'))
    if token is None:
        return '{"error":"token error"}', 403
    try:
        e_type = request.args.get('type')
        if not e_type == 'fr' and not e_type =='fl':
            return Response('{"error":"invalid parameter"}', status=400)

        entity = entity_type(e_type)
        delete_response = entity.delete(id, user_id)
        resp = Response(response='{"status":"' + delete_response + '"}',
                    status=200 if delete_response == "success" else 500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp


def move_entity(id, user_id):
    token = token_validator(request.headers.get('token'))
    if token is None:
        return '{"error":"token error"}', 403
    try:
        e_type = request.args.get('type')
        if not e_type == 'fr' and not e_type =='fl':
            return Response('{"error":"invalid parameter"}', status=400)

        parent_name = request.form['parent_name']
        entity = entity_type(e_type)

        move_response = entity.move(id, user_id, parent_name)
        resp = Response(response='{"status":"' + move_response + '"}',
                    status=200 if move_response == "success" else 500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp
