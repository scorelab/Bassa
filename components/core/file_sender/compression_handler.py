import sys
import zipfile
import os
from os.path import basename
import logging
from DownloadManager import set_compression_progress, get_id_from_gid, get_download_path, insert_compression_process
import json
import time


def compress(file_list, file_name):
	logging.info('Compression starts of filename {0}, which consists following files {1}'.format(file_name, file_list))
	try:
		timestamp = time.time()
		status = insert_compression_process(comp_id=file_name, start_time=timestamp, completed_time=timestamp, is_deleted=0)
		zip_path = get_zip_path(file_name)
		zip_file = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_STORED)
		set_compression_progress(comp_id=file_name, status=status, completed_time=timestamp)
		for file in file_list:
			if os.path.exists(file):
				logging.info("file: %s", file)
				zip_file.write(file, basename(file))
		zip_file.close()
		logging.info('Compression of files is done, written to following file {0}'.format(zip_path))
		set_compression_progress(comp_id=file_name, status=1, completed_time=time.time())
		return zip_path
	except Exception as e:
		logging.error('Exception occurred during compression {0}'.format(e))


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
	zip_path = os.path.join(tmp_dir, file_name_formatter(file_name) + '.zip')
	return zip_path


def file_name_formatter(file_name):
	if len(file_name) > 250:  # leaved 5 characters for file extension type
		file_name = file_name[:250]
	return file_name


if __name__ == "__main__":
	logging.basicConfig(filename="./debug-server.log", level=logging.DEBUG)
	gid_list = sys.argv
	logging.info("before pop %s", gid_list)
	gid_list.pop(0)  # remove file name as an argument
	logging.info("after pop %s", gid_list)
	gid_list.sort()
	file_path_list = []
	ugid_of_compressed_file = ''
	for elem in gid_list:
		ugid_of_compressed_file += elem
		id = get_id_from_gid(elem)
		download_path = get_download_path(id)
		file_path_list.append(download_path)
	logging.info(file_path_list)
	compress(file_path_list, ugid_of_compressed_file)
