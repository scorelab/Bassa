from flask import Flask
from flask.ext.cors import CORS
from flask import send_file, send_from_directory
from flask import request, jsonify, abort, Response, g
from flask_socketio import SocketIO, join_room
from Auth import *
from Models import *
from DownloadManager import *
import json, urllib.request, urllib.error, urllib.parse, _thread
from multiprocessing import Process
from DownloadDaemon import starter
from EMail import send_mail
from gevent import monkey
from Server import *
from file_sender import sender


@server.route('/download/start')
def start():
	try:
		token = request.headers['key']
		if str(token) != server.config['SECRET_KEY']:
			return "{'error':'not authorized'}", 403
		global p
		p = Process(target=starter, args=(socketio,))
		p.start()
		return '{"status":"' + str(p.pid) + '"}'
	except Exception as e:
		return '{"error":"' + e.message + '"}', 400


@socketio.on('join', namespace='/progress')
def on_join(data):
	room = data['room']
	if room != '':
		join_room(room)


@server.route('/download/kill')
def kill():
	try:
		token = request.headers['key']
		if str(token) != server.config['SECRET_KEY']:
			return "{'error':'not authorized'}", 403
		if p is not None:
			p.terminate()
			p.join()
			jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 'qwer', 'method': 'aria2.pauseAll'})
			jsonreq = jsonreq.encode('ascii')
			c = urllib.request.urlopen('http://localhost:6800/jsonrpc', jsonreq)
			if verbose:
				print(c)
		if not p.is_alive():
			return '{"status":"success"}'
		else:
			return '{"error":"error"}'
	except Exception as e:
		return '{"error":"' + e.message + '"}', 400


@server.route('/api/download', methods=['POST'])
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
			resp = Response(response='{"error":"' + e.message + '"}', status=400)
		resp.headers['token'] = token
		resp.headers['Access-Control-Expose-Headers'] = 'token'
		return resp
	elif token is not None:
		return '{"error":"not authorized"}', 403
	else:
		return '{"error":"token error"}', 403


@server.route('/api/download/<int:id>', methods=['DELETE'])
def remove_download_request(id):
	token = token_validator(request.headers['token'])
	if token is not None:
		try:
			status = remove_download(id, g.user.userName)
			resp = Response(response='{"status":"' + status + '"}', status=(200 if status == "success" else 400))
		except Exception as e:
			resp = Response(response='{"error":"' + e.message + '"}', status=400)
		resp.headers['token'] = token
		resp.headers['Access-Control-Expose-Headers'] = 'token'
		return resp
	elif token is not None:
		return '{"error":"not authorized"}', 403
	else:
		return '{"error":"token error"}', 403


@server.route('/api/download/rate/<int:id>', methods=['POST'])
def rate_download_request(id):
	token = token_validator(request.headers['token'])
	if token is not None:
		data = request.get_json(force=True)
		try:
			status = rate_download(id, g.user.userName, data['rate'])
			resp = Response(response='{"status":"' + status + '"}', status=(200 if status == "success" else 400))
		except Exception as e:
			resp = Response(response='{"error":"' + e.message + '"}', status=400)
		resp.headers['token'] = token
		resp.headers['Access-Control-Expose-Headers'] = 'token'
		return resp
	elif token is not None:
		return '{"error":"not authorized"}', 403
	else:
		return '{"error":"token error"}', 403


@server.route('/api/downloads/<int:limit>', methods=['GET'])
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
			resp = Response(response='{"error":"' + e.message + '"}', status=400)
		resp.headers['token'] = token
		resp.headers['Access-Control-Expose-Headers'] = 'token'
		return resp
	elif token is not None:
		return '{"error":"not authorized"}', 403
	else:
		return '{"error":"token error"}', 403


@server.route('/api/download/<int:id>', methods=['GET'])
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
			resp = Response(response="{'error':'" + e.message + "'}", status=400)
			return resp
	elif token is not None:
		return '{"error":"not authorized"}', 403
	else:
		return '{"error":"token error"}', 403


# register endpoints
server.add_url_rule('/api/file', 'send_file_from_path', sender.send_file_from_path, methods=['GET'])
server.add_url_rule('/api/compress', 'start_compression', sender.start_compression, methods=['POST'])
server.add_url_rule('/api/compression-progress', 'get_compression_progress', sender.check_compression_progress, methods=['GET'])
