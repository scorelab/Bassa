from flask import json
from flask import request, abort, Response, g
from utils.token_utils import token_validator
from managers.NotifManager import *

def fetch_notifs(user_id):
    token = token_validator(request.headers.get('token'))
    if token is None:
        return '{"error":"token error"}', 403
    try:
        notif_response = get_notif(user_id)
        if not isinstance(notif_response, str):
            resp = Response(response=json.dumps(notif_response), status=200)
        else:
            resp = Response('{"error":"' + notif_response + '"}', status=500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp

def save_notif(user_name):
    token = token_validator(request.headers.get('token'))
    if token is None:
        return '{"error":"token error"}', 403
    try:
        notif = request.form.get('notif')

        post_response = post_notif(user_name, notif)
        resp = Response(response='{"status":"' + post_response + '"}',
                    status=200 if post_response == "success" else 500)
    except Exception as e:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp