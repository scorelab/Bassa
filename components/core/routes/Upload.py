import json
import requests
from flask import request, Response
from file_handler.uploader import upload_file_helper
from managers.DirectoryManager import File
from utils.token_utils import token_validator


def upload_file_to_server(user_id, parent_id):
    token = token_validator(request.headers.get('token'))
    if token is None:
        return '{"error":"token error"}', 403
    try:

        file_to_upload = request.files['file']
        e_type = 'fl'

        upload_response = upload_file_helper(file_to_upload)

        if not 'msg' in upload_response:
            return Response(response='{"error":"'+ upload_response['err'] +'"}', status=500)

        elif upload_response['msg'] is not 'success':
            return Response(response='{"error":"' + upload_response['msg'] + '"}', status=400)

        name = upload_response['name']
        path = upload_response['path']
        add_response = File().create(name, user_id, parent_id, path)

        if add_response is 'success':
            res = Response(response='{"status":"'+ add_response +'", "ext":"'+ upload_response['ext'] +'"}', status=200)
        else:
            res = Response(response='{"error":"' + add_response + '"}', status=400)

    except Exception as e:
        res = Response('{"error":"' + str(e) + '"}', status=400)

    res.headers['token'] = token
    res.headers['Access-Control-Expose-Headers'] = 'token'
    return res

