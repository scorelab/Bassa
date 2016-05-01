from Models import Download, Status
from DBCon import *
import time


def add_download(download):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT into download(link, user_name, added_time) VALUES(%s, %s, %s);"
        try:
            cursor.execute(sql, (download.link, download.userName, int(time.time())))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"


def remove_download(id, userName):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql1 = "SELECT status FROM download WHERE id=%s;"
        sql = "DELETE from download WHERE id=%s and user_name=%s;"
        try:
            cursor.execute(sql1, id)
            data = cursor.fetchone()
            if data[0] != Status.DEFAULT and data[0] != Status.ERROR:
                db.commit()
                return "Download started. Entry cannot be deleted."
            cursor.execute(sql, (id, userName))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"


def rate_download(id, userName, rate):
    if rate > 5 or rate < 0:
        return "Value error"
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql1 = "UPDATE rate SET rate=%s WHERE id=%s AND user_name=%s;"
        sql = "INSERT INTO rate VALUES(%s, %s, %s);"
        try:
            cursor.execute(sql1, (rate, id, userName))
            if cursor.rowcount == 0:
                cursor.execute(sql, (userName, id, rate))
            db.commit()
            update_rate(id)
        except MySQLdb.Error as e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"


def update_rate(id):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE download SET rating=%s WHERE id=%s ;"
        sql1 = "SELECT ROUND(AVG(rate),0) AS rating FROM rate WHERE id=%s;"
        try:
            cursor.execute(sql1, id)
            data = cursor.fetchone()
            cursor.execute(sql, (data[0], id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"


def get_downloads_user(userName, limit):
    recordsPerPage = 15
    db = get_db_con()
    if db is not None:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM download WHERE user_name=%s ORDER by 'added_time' LIMIT %s, %s;"
        try:
            cursor.execute(sql, (userName, (limit - 1) * recordsPerPage, limit * recordsPerPage))
            results = cursor.fetchall()
            db.commit()
            return results
        except MySQLdb.Error as e:
            return e[1]
    return "db connection error"


def get_downloads(limit):
    recordsPerPage = 15
    db = get_db_con()
    if db is not None:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM download WHERE status=3 ORDER by 'added_time' DESC LIMIT %s, %s;"
        try:
            cursor.execute(sql, ((limit - 1) * recordsPerPage, limit * recordsPerPage))
            results = cursor.fetchall()
            db.commit()
            return results
        except MySQLdb.Error as e:
            return e[1]
    return "db connection error"


def update_status_gid(gid, status, completed=False):
    db = get_db_con()
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
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"


def set_gid(id, gid):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE download SET gid=%s WHERE id=%s ;"
        try:
            cursor.execute(sql, (gid, id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"


def get_to_download():
    db = get_db_con()
    if db is not None:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT link, id FROM download WHERE status=0 ORDER by 'added_time' LIMIT 1;"
        try:
            cursor.execute(sql)
            if cursor.rowcount == 0:
                return None
            results = cursor.fetchone()
            download = Download(results['link'], None)
            download.id = results['id']
            db.commit()
            return download
        except MySQLdb.Error as e:
            return e[1]
    return "db connection error"

def set_path(gid, path):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE download SET path=%s WHERE gid=%s ;"
        try:
            cursor.execute(sql, (path, gid))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"

def get_download_path(id):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT path FROM download WHERE status=3 AND id=%s LIMIT 1;"
        try:
            cursor.execute(sql, (id))
            if cursor.rowcount == 0:
                return None
            results = cursor.fetchone()
            path = results['path']
            db.commit()
            return path
        except MySQLdb.Error as e:
            return e[1]
    return "db connection error"

def get_download_email(gid):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT user.email FROM user LEFT JOIN download ON user.user_name = download.user_name WHERE download.gid=%s LIMIT 1;"
        try:
            cursor.execute(sql, gid)
            if cursor.rowcount == 0:
                return None
            results = cursor.fetchone()
            path = results['email']
            db.commit()
            return path
        except MySQLdb.Error as e:
            return e[1]
    return "db connection error"

def get_to_delete(time, rate):
    recordsPerPage = 15
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT path FROM  download  WHERE  completed_time <%s AND  rating <=%s AND status=3;"
        try:
            cursor.execute(sql, (time, rate))
            results = cursor.fetchall()
            db.commit()
            return results
        except MySQLdb.Error as e:
            return e[1]
    return "db connection error"

def set_delete_status(path):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE download SET status=2 WHERE path=%s ;"
        try:
            cursor.execute(sql, path)
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"