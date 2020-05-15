from Models import Download, Status
from DBCon import *
import time
import sys
import sqlalchemy.pool as pool
import logging

verbose = False

if len(sys.argv) == 2 and sys.argv[1] == '-v':
	verbose = True

threadpool = pool.QueuePool(get_db_con, max_overflow=10, pool_size=0)


def add_download(download):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		if download.link.split(':')[0] == "magnet":
			download_name = download.link.split('&')[1].split('=')[1]
		else:
			download_name = download.link.split('/')[-1]
		sql = "INSERT into download(link, user_name, added_time, download_name) VALUES(%s, %s, %s, %s);"
		try:
			cursor.execute(sql, (download.link, download.userName, int(time.time()), download_name))
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def remove_download(id, userName):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql1 = "SELECT status FROM download WHERE id=%s;"
		sql = "DELETE from download WHERE id=%s and user_name=%s;"
		try:
			cursor.execute(sql1, [str(id)])
			data = cursor.fetchone()
			cursor.close()
			if data[0] != Status.DEFAULT and data[0] != Status.ERROR:
				db.commit()
				db.close()
				return "Download started. Entry cannot be deleted."
			cursor = db.cursor()
			cursor.execute(sql, [str(id), userName])
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def rate_download(id, userName, rate):
	if rate > 5 or rate < 0:
		return "Value error"
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql1 = "UPDATE rate SET rate=%s WHERE id=%s AND user_name=%s;"
		sql = "INSERT INTO rate VALUES(%s, %s, %s);"
		try:
			cursor.execute(sql1, (rate, id, userName))
			if cursor.rowcount == 0:
				cursor.execute(sql, (userName, id, rate))
			cursor.close()
			db.commit()
			db.close()
			update_rate(id)
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def update_rate(id):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql = "UPDATE download SET rating=%s WHERE id=%s ;"
		sql1 = "SELECT ROUND(AVG(rate),0) AS rating FROM rate WHERE id=%s;"
		try:
			cursor.execute(sql1, id)
			data = cursor.fetchone()
			cursor.execute(sql, (data[0], id))
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def get_downloads_user(userName, limit):
	recordsPerPage = 15
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT * FROM download WHERE user_name=%s ORDER by 'added_time' LIMIT %s, %s;"
		try:
			cursor.execute(sql, (userName, (limit - 1) * recordsPerPage, limit * recordsPerPage))
			results = cursor.fetchall()
			db.close()
			return results
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def get_downloads(limit):
	recordsPerPage = 15
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT * FROM download WHERE status=3 ORDER by 'added_time' DESC LIMIT %s, %s;"
		try:
			cursor.execute(sql, ((limit - 1) * recordsPerPage, limit * recordsPerPage))
			results = cursor.fetchall()
			db.close()
			return results
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def update_status_gid(gid, status, completed=False):
	print("Update status", gid, status, completed)
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql = "UPDATE download SET status=%s WHERE gid=%s ;"
		if completed:
			sql = "UPDATE download SET status=%s, completed_time=%s WHERE gid=%s ;"
		try:
			if completed:
				cursor.execute(sql, (status, int(time.time()), gid))
			else:
				cursor.execute(sql, (status, gid))
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def set_gid(id, gid):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql = "UPDATE download SET gid='%s' WHERE id=%s;" % (gid, id)
		try:
			cursor.execute(sql)
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def set_name(gid, name):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql = "UPDATE download SET download_name=%s WHERE gid=%s ;"
		try:
			cursor.execute(sql, (name, gid))
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def set_size(gid, size):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql = "UPDATE download SET size=%s WHERE gid=%s ;"
		try:
			cursor.execute(sql, (size, gid))
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def get_to_download():
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT link, id, user_name FROM download WHERE status=0 ORDER by 'added_time';"
		try:
			cursor.execute(sql)
			if cursor.rowcount == 0:
				if verbose: print("zero count")
				return None
			results = cursor.fetchall()
			cursor.close()
			db.close()
			if verbose: print("LIST", results)
			downloads = [Download(result['link'], result['user_name'], result['id']) for result in results]
			return downloads
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def set_path(gid, path):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql = "UPDATE download SET path=%s WHERE gid=%s ;"
		try:
			cursor.execute(sql, (path, gid))
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def get_download_path(id):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT path FROM download WHERE status=3 AND id=%s LIMIT 1;"
		try:
			cursor.execute(sql, (id,))
			if cursor.rowcount == 0:
				return None
			results = cursor.fetchone()
			cursor.close()
			path = results['path']
			db.close()
			return path
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def get_download_email(gid):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT user.email FROM user LEFT JOIN download ON user.user_name = download.user_name WHERE download.gid=%s LIMIT 1;"
		try:
			cursor.execute(sql, gid)
			if cursor.rowcount == 0:
				return None
			results = cursor.fetchone()
			cursor.close()
			path = results['email']
			db.close()
			return path
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def get_to_delete(time, rate):
	recordsPerPage = 15
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql = "SELECT path FROM  download  WHERE  completed_time <%s AND  rating <=%s AND status=3;"
		try:
			cursor.execute(sql, (time, rate))
			results = cursor.fetchall()
			cursor.close()
			db.close()
			if verbose: print("Time", time, "Rate", rate)
			if verbose: print("results", results)
			return results
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def set_delete_status(path):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql = "UPDATE download SET status=2 WHERE path='%s' ;" % path
		try:
			cursor.execute(sql)
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def get_download_status(id):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT status FROM download WHERE id='%s';" % id
		try:
			cursor.execute(sql)
			if cursor.rowcount == 0:
				return None
			results = cursor.fetchone()
			cursor.close()
			print('results')
			status = results['status']
			db.close()
			return status
		except MySQLdb.Error as e:
			raise
	return "db connection error"


def get_id_from_gid(gid):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT id FROM download WHERE gid='%s';" % gid
		try:
			cursor.execute(sql)
			if cursor.rowcount == 0:
				return None
			results = cursor.fetchone()
			cursor.close()
			status = results['id']
			db.close()
			return status
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def get_username_from_gid(gid):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT user_name FROM download WHERE gid='%s';" % gid
		try:
			cursor.execute(sql)
			if cursor.rowcount == 0:
				return None
			results = cursor.fetchone()
			cursor.close()
			status = results['user_name']
			db.close()
			return status
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def get_gid_from_id(id):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT gid FROM download WHERE id='%s';" % id
		try:
			cursor.execute(sql)
			if cursor.rowcount == 0:
				return None
			results = cursor.fetchone()
			cursor.close()
			gid = results['gid']
			db.close()
			return gid
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def get_download_name_from_id(id):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT download_name FROM download WHERE id='%s';" % id
		try:
			cursor.execute(sql)
			if cursor.rowcount == 0:
				return None
			results = cursor.fetchone()
			cursor.close()
			download_name = results['download_name']
			db.close()
			return download_name
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def set_compression_progress(comp_id, status, **kwargs):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		if kwargs is None:
			sql = "UPDATE compression SET progress = {} WHERE id = '{}'".format(status, comp_id)
		else:
			sql = "UPDATE compression SET progress = {}, completed_time = {} WHERE id = '{}'".format(status, kwargs[
				'completed_time'], comp_id)
		try:
			cursor.execute(sql, )
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return "success"
	return "db connection error"


def get_compression_progress(comp_id):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT progress FROM compression WHERE id = '%s' LIMIT 1" % comp_id
		try:
			cursor.execute(sql, )
			if cursor.rowcount == 0:
				return None
			results = cursor.fetchone()
			cursor.close()
			status = results['progress']
			db.close()
			return status
		except MySQLdb.Error as e:
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"


def insert_compression_process(comp_id, start_time, completed_time, is_deleted):
	# deleted is tinyint, either 0(false) or 1(true)
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "INSERT INTO compression (`id`, `progress`, `start_time`, `completed_time`, `deleted`) VALUES ('{}', 0, {}, {}, {} )".format(
			comp_id, start_time, completed_time, is_deleted)
		try:
			cursor.execute(sql, )
			cursor.close()
			db.commit()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			logging.error("Error %d: %s", e.args[0], e.args[1])
		return 0
	return "db connection error"

def update_minio_indexes(file_name, file_path, gid, completedLength, username, download_id):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor()
		sql = "INSERT into minio(mid, mgid, muser_name, mfile_name, msize, mpath) VALUES(%s, %s, %s, %s, %s, %s);"
		try:
			cursor.execute(sql, (download_id, gid, username, file_name, completedLength, file_path))
			db.commit()
			cursor.close()
			db.close()
		except MySQLdb.Error as e:
			db.rollback()
			# Shows error thrown up by database
			print(e)

def get_file_name(id):
	db = threadpool.connect()
	if db is not None:
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		sql = "SELECT mfile_name FROM minio WHERE mid='%s';" % id
		print(sql)
		try:
			cursor.execute(sql)
			if cursor.rowcount == 0:
				return None
			results = cursor.fetchone()
			print(results)
			cursor.close()
			file_name = results['mfile_name']
			db.close()
			return file_name
		except MySQLdb.Error as e:
			print(e)
			logging.error("Error %d: %s", e.args[0], e.args[1])
	return "db connection error"
