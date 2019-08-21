from flask import send_file
from flask import request, Response, g
from Auth import *
from managers.DownloadManager import *
import json, urllib.request, urllib.error, urllib.parse
from multiprocessing import Process
from DownloadDaemon import starter
from utils.app_constants import SERVER_SECRET_KEY
from utils.token_utils import token_validator
from initializer import socketio
conf = get_conf_reader("dl.conf")

def start():
	try:
		token = request.headers['key']
		if str(token) != SERVER_SECRET_KEY:
			return "{'error':'not authorized'}", 403
		global p
		p = Process(target=starter, args=(socketio,))
		p.start()
		return '{"status":"' + str(p.pid) + '"}'
	except Exception as e:
		return '{"error":"' + str(e) + '"}', 400


def kill():
	try:
		token = request.headers['key']
		if str(token) != SERVER_SECRET_KEY:
			return "{'error':'not authorized'}", 403
		if p is not None:
			p.terminate()
			p.join()
			jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 'qwer', 'method': 'aria2.pauseAll'})
			jsonreq = jsonreq.encode('ascii')
			c = urllib.request.urlopen(conf['aria_server'], jsonreq)
			if verbose:
				print(c)
		if not p.is_alive():
			return '{"status":"success"}'
		else:
			return '{"error":"error"}'
	except Exception as e:
		return '{"error":"' + str(e) + '"}', 400


def add_download_request():
	token = token_validator(request.headers['token'])
	if token is not None:
		data = request.get_json(force=True)
		try:
			if check_if_bandwidth_exceeded(g.user.userName):
				resp = Response(response='{"quota":"exceeded"}', status=400)
			else:
				newDownload = Download(data['link'], g.user.userName)
				status = add_download(newDownload)
				resp = Response(response='{"status":"' + status + '"}', status=200 if status == "success" else 400)
		except Exception as e:
			resp = Response(response='{"error":"' + str(e) + '"}', status=400)
		resp.headers['token'] = token
		resp.headers['Access-Control-Expose-Headers'] = 'token'
		return resp
	elif token is not None:
		return '{"error":"not authorized"}', 403
	else:
		return '{"error":"token error"}', 403


def remove_download_request(id):
	token = token_validator(request.headers['token'])
	if token is not None:
		try:
			status = remove_download(id, g.user.userName)
			resp = Response(response='{"status":"' + status + '"}', status=(200 if status == "success" else 400))
		except Exception as e:
			resp = Response(response='{"error":"' + str(e) + '"}', status=400)
		resp.headers['token'] = token
		resp.headers['Access-Control-Expose-Headers'] = 'token'
		return resp
	elif token is not None:
		return '{"error":"not authorized"}', 403
	else:
		return '{"error":"token error"}', 403


def rate_download_request(id):
	token = token_validator(request.headers['token'])
	if token is not None:
		data = request.get_json(force=True)
		try:
			status = rate_download(id, g.user.userName, data['rate'])
			resp = Response(response='{"status":"' + status + '"}', status=(200 if status == "success" else 400))
		except Exception as e:
			resp = Response(response='{"error":"' + str(e) + '"}', status=400)
		resp.headers['token'] = token
		resp.headers['Access-Control-Expose-Headers'] = 'token'
		return resp
	elif token is not None:
		return '{"error":"not authorized"}', 403
	else:
		return '{"error":"token error"}', 403


def get_downloads_request(limit):
	token = token_validator(request.headers['token'])
	if token is not None:
		try:
			status = get_downloads(int(limit))
			if not isinstance(status, str):
				resp = Response(response=json.dumps(status), status=200)
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


def get_download(id):
	token = token_validator(request.headers['token'])
	if token is not None:
		try:
			status = get_download_path(int(id))
			if status is not None and status != "db connection error":
				if verbose:
					print(status)
				return send_file(status, as_attachment=True, mimetype='multipart/form-data')
			else:
				return '{"error":"file not found"}', 404
		except Exception as e:
			resp = Response(response="{'error':'" + str(e) + "'}", status=400)
			return resp
	elif token is not None:
		return '{"error":"not authorized"}', 403
	else:
		return '{"error":"token error"}', 403
