from flask import request, Response, g
from Models import *
from DirectoryManager import *
from utils.token_utils import token_validator

##################### workspace endpoints ######################

def fetch_workspaces(user_id):
    user_id = int(user_id)
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = get_workspaces(user_id)
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response('{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403

def fetch_workspace(workspace_id, user_id):
    user_id = int(user_id)
    workspace_id = int(workspace_id)
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = get_workspace_by_id(workspace_id, user_id)
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response('{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403

def add_workspace(name, user_id):
    user_id = int(user_id)
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = create_workspace(name, user_id)
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response('{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403

def edit_workspace(name, workspace_id, user_id):
    workspace_id = int(workspace_id)
    user_id = int(user_id)
    if token is not None:
        try:
            status = update_workspace(name, user_id)
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response('{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403

##################### project endpoints ######################

def fetch_projects(workspace_id):
    workspace_id = int(workspace_id)
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = get_projects(workspace_id)
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response('{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403

def fetch_project(project_id, workspace_id):
    project_id = int(project_id)
    workspace_id = int(workspace_id)
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = get_project_by_id(project_id, workspace_id)
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response('{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403

def add_project(name, workspace_id):
    workspace_id = int(workspace_id)
    token = token_validator(request.headers['token'])
    if token is not None:
        try:
            status = create_project(name, workspace_id)
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response('{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403

def edit_project(name, project_id, workspace_id):
    project_id = int(project_id)
    workspace_id = int(workspace_id)
    if token is not None:
        try:
            status = update_project(name, project_id, workspace_id)
            if not isinstance(status, str):
                resp = Response(response=json.dumps(status), status=200)
            else:
                resp = Response('{"error":"' + status + '"}', status=400)
        except Exception as e:
            resp = Response('{"error":"' + str(e) + '"}', status=400)
        resp.headers['token'] = token
        resp.headers['Access-Control-Expose-Headers'] = 'token'
        return resp
    elif token is not None:
        return '{"error":"not authorized"}', 403
    else:
        return '{"error":"token error"}', 403
