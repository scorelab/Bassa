from Models import Download, Status
from DBCon import *
import time


def add_download(download):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT into download(link, user_name, added_time) VALUES(%s, %s, %s);"
        try:
            cursor.execute(sql, (download.link, download.userName, time.time()))
            db.commit()
        except MySQLdb.Error, e:
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
            if data[0]!=Status.DEFAULT and data[0]!=Status.ERROR :
                db.commit()
                return "Download started. Entry cannot be deleted."
            cursor.execute(sql, (id, userName))
            db.commit()
        except MySQLdb.Error, e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"

def rate_download(id, userName, rate):
    if rate>5 or rate<0:
        return "Value error"
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql1 = "UPDATE rate SET rate=%s WHERE id=%s AND user_name=%s;"
        sql = "INSERT INTO rate VALUES(%s, %s, %s);"
        try:
            cursor.execute(sql1, (rate, id, userName))
            if cursor.rowcount==0 :
                cursor.execute(sql, (userName, id, rate))
            db.commit()
            update_rate(id)
        except MySQLdb.Error, e:
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
            print data[0]
            cursor.execute(sql, (data[0], id))
            db.commit()
        except MySQLdb.Error, e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"

def get_downloads_user(userName, limit):
    recordsPerPage=15
    db = get_db_con()
    if db is not None:
        cursor =  db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM download WHERE user_name=%s ORDER by 'added_time' LIMIT %s, %s;"
        try:
            cursor.execute(sql, (userName,(limit-1)*recordsPerPage, limit*recordsPerPage))
            results = cursor.fetchall()
            db.commit()
            return results
        except MySQLdb.Error, e:
            return e[1]
    return "db connection error"

def get_downloads(limit):
    recordsPerPage=15
    print limit
    db = get_db_con()
    if db is not None:
        cursor =  db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM download WHERE status=3 ORDER by 'added_time' LIMIT %s, %s;"
        try:
            cursor.execute(sql, ((limit-1)*recordsPerPage, limit*recordsPerPage))
            results = cursor.fetchall()
            db.commit()
            return results
        except MySQLdb.Error, e:
            return e[1]
    return "db connection error"