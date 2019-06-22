from flask import Response, request
from DownloadDaemon import *
from minio import Minio
from minio.error import ResponseError
from DownloadManager import *
from DBCon import *
import sys
import sqlalchemy.pool as pool

client = Minio('localhost:9000', secure=False,
               access_key='bassa',
                  secret_key='bassa123')

def upload_to_minio(file_name, file_path):
	fname = file_name
	fpath = file_path
	try:
		client.fput_object('bassa', fname, fpath)
	except ResponseError as err:
		print(err)


def update_minio_indexes(file_name, file_path, gid, completedLength, username, download_id):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		m_fname = file_name
		m_fpath = file_path
		m_id = download_id
		m_gid = gid
		m_size = completedLength
		m_username = username
		sql = "INSERT into minio(mid, mgid, muser_name, mfile_name, msize, mpath) VALUES(%s, %s, %s, %s, %s, %s);"
		try:
			cursor.execute(sql, (m_id, m_gid, m_username, m_fname, m_size, m_fpath))
			db.commit()
		except MySQLdb.Error as e:
			db.rollback()
			# Shows error thrown up by database
			print(e)
