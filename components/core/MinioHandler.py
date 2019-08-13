from DownloadDaemon import *
from minio import Minio
from minio.error import ResponseError

client = Minio('localhost:9000', secure=False,
               access_key='bassa',
                  secret_key='bassa123')

def upload_to_minio(file_name, file_path):
	try:
		bucket_status = client.bucket_exists('bassa')
		#print(bucket_status)
		if not bucket_status:
			client.make_bucket('bassa')
		client.fput_object('bassa', file_name, file_path)
	except ResponseError as err:
		print(err)

def get_file_url(fname):
	try:
		file_url = client.presigned_get_object('bassa', fname)
		return file_url
	except ResponseError as err:
		return err
