from flask import Response, request
from DownloadDaemon import *
from minio import Minio
from minio.error import ResponseError

def upload_to_minio(file_name, file_path):
	client = Minio('localhost:9000', secure=False,
               access_key='2N2XFGY92ML8JMXGB2M4',
                  secret_key='a6Nsx+lRtj3Cm9lxO1JW3xqHXG+sIKmunNIl1U7V')
	fname = file_name
	fpath = file_path
	try:
		client.fput_object('bassa', fname, fpath)
	except ResponseError as err:
		print(err)
	