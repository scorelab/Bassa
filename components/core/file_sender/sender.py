from flask import Response, request, send_file, jsonify
from DownloadManager import get_id_from_gid, get_download_path, get_download_name_from_id, get_compression_progress
import logging
import os
import subprocess
import json
from utils.token_utils import token_validator


def send_file_from_path():
	token = None
	if request.args.get('share') is not None:
		token = 'sample-token-for-sharing-feature'
	if token is None:
		token = token_validator(request.headers['token'])
	if token is not None:
		try:
			gid = request.args.get('gid')
			logging.info('User asked for file, having GID (ugid) ' + gid)
			file_name = file_name_formatter(gid) + '.zip'
			download_path = get_zip_path(gid)
		except Exception as e:
			logging.error(" get file API (/api/file) got wrong arguments, thrown an error :: %s" % e)
			return Response("error", status=400)
		
		try:
			return send_file(filename_or_fp=download_path, attachment_filename=file_name,
							 as_attachment=True)
		except Exception as e:
			logging.error("File sending has a exception. When sending file, we got :: %s" % e)
			return Response("File you are trying to access is not available to us. Please ask admin to check the server"
							, status=404)
	else:
		return Response("Invalid Token in request", 403)


def dl_config_reader():
	script_path = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(script_path, "../dl.conf")
	conf_str = ''
	with open(path, 'r') as conf_file:
		conf_str = conf_file.read()
		conf_file.close()
	return json.loads(conf_str)


def get_zip_path(file_name):
	conf_json = dl_config_reader()
	tmp_dir = conf_json['tmp_folder']
	if not os.path.exists(tmp_dir):  # check tmp directory exists or not
		os.makedirs(tmp_dir)
	zip_path = os.path.join(tmp_dir , file_name_formatter(file_name) + '.zip')
	return zip_path


def file_name_formatter(file_name):
	if len(file_name) > 250:  # leaved 5 characters for file extension type
		file_name = file_name[:250]
	return file_name


def start_compression():
	token = None
	if request.args.get('share') is not None:
		token = 'sample-token-for-sharing-feature'
	if token is None:
		token = token_validator(request.headers['token'])
	if token is not None:
		gid_list = request.get_json()['gid']  # list of file identifiers to compress
		gid_list.sort()
		ugid_of_compressed_file = ''
		subprocess_params = ''  # parameters required to start compression handler
		for elem in gid_list:
			ugid_of_compressed_file += elem
			subprocess_params += elem + ' '
		# check status of file existence
		if os.path.exists(get_zip_path(ugid_of_compressed_file)):
			response_dict = {'process_id': ugid_of_compressed_file, 'progress': get_compression_progress(ugid_of_compressed_file)}
			return jsonify(response_dict)

		script_path = os.path.abspath(os.path.dirname(__file__))
		subprocess.call("python3 {}/compression_handler.py {} &".format(script_path, subprocess_params), shell=True)
		response_dict = {'process_id': ugid_of_compressed_file, 'progress': 0}
		return jsonify(response_dict)
	else:
		return Response("Invalid Token in request", 403)
	

def check_compression_progress():
	token = token_validator(request.headers['token'])
	if token is not None:
		process_id = request.args.get('gid')
		status = get_compression_progress(comp_id=process_id)
		response_dict = {'process_id': process_id, 'progress': status}
		return jsonify(response_dict)
	else:
		return Response("Invalid Token in request", 403)
