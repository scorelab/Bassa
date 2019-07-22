import json
import requests
from flask import request, Response
from file_handler.uploader import upload_file_helper, headers
from utils.token_utils import token_validator


def upload_file_to_server(user_id):
    token = token_validator(request.headers.get('token'))
    if token is None:
        return '{"error":"token error"}', 403
    try:
        form_field = request.form.get('field')
        parent_id = request.form.get('parent_id')
        e_type = request.args.get('type')
        token_dict = { 'token': token }

        headers.update(token_dict)
        upload_response = upload_file_helper(form_field)

        if not 'msg' in upload_response:
            resp = Response(response='{"error":"'+ upload_response['err'] +'"}', status=500)

        if upload_response['msg'] is not 'success':
            resp = Response(response='{"error":"' + upload_response['msg'] + '"}', status=400)

        file_body = "name="+upload_response['name']+"&parent_id="+parent_id
        add_response = requests.post('http://localhost:5000/api/user/drive/'+user_id+'/add', file_body, params=e_type, headers=add_headers)
        data = json.loads(add_response)

        if add_response.status is '500':
            resp = Response(response='{"error":"'+ data['status'] +'"}', status=500)
        elif add_response.status is '400':
            resp = Response(response='{"error":"'+ data['error'] +'"}', status=400)
        else:
            resp = Response(response='{"status":"' + data['status'] + '"}', status=200)
    except:
        resp = Response('{"error":"' + str(e) + '"}', status=400)
    resp.headers['token'] = token
    resp.headers['Access-Control-Expose-Headers'] = 'token'
    return resp

