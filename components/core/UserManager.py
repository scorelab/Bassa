from Models import User
from DBCon import *
from ConfReader import get_conf_reader
import sqlalchemy.pool as pool
import logging

conf = get_conf_reader("dl.conf")

threadpool = pool.QueuePool(get_db_con, max_overflow=10, pool_size=0)

def user_login(username, password):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT * FROM user WHERE user_name=%s AND password=MD5(%s) AND blocked=0;"
        cursor.execute(sql, (username, password))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        if data == None:
            return False
        else:
            return True

def check_approved(username, password):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT * FROM user WHERE user_name=%s AND password=MD5(%s) AND approved=1;"
        cursor.execute(sql, (username, password))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        if data == None:
            return False
        else:
            return True

def check_user_name(username):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT * FROM user WHERE user_name=%s;"
        cursor.execute(sql, (username))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        if data == None:
            return False
        else:
            return True


def get_user(username):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM user WHERE user_name='%s' and blocked=0;" % username
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        db.close()
        if data == None:
            return None
        else:
            return User(data['user_name'], data['password'], data['auth'], data['email'])


def add_user(user):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT into user VALUES(%s, MD5(%s), %s, %s, 0, 0);"
        try:
            cursor.execute(sql, (user.userName, user.password, user.auth, user.email))
            cursor.close()
            db.commit()
            db.close()
        except MySQLdb.Error as e:
            db.rollback()
            logging.error("Error %d: %s", e.args[0], e.args[1])
        return "success"
    return "db connection error"

def add_regular_user(user):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT into user VALUES(%s, MD5(%s), %s, %s, 0, 0);"
        try:
            cursor.execute(sql, (user.userName, user.password, user.auth, user.email))
            cursor.close()
            db.commit()
            db.close()
        except MySQLdb.IntegrityError:
            db.rollback()
            return "username taken"
        return "success"
    return "db connection error"

def remove_user(username):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "DELETE from user WHERE user_name=%s;"
        try:
            cursor.execute(sql, (username))
            cursor.close()
            db.commit()
            db.close()
        except MySQLdb.Error as e:
            db.rollback()
            logging.error("Error %d: %s", e.args[0], e.args[1])
        return "success"
    return "db connection error"


def update_user(user, username):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE user SET user_name=%s, auth=%s, email=%s WHERE user_name=%s;"
        try:
            cursor.execute(sql, (user.userName, user.auth, user.email, username))
            cursor.close()
            db.commit()
            db.close()
        except MySQLdb.Error as e:
            db.rollback()
            logging.error("Error %d: %s", e.args[0], e.args[1])
        return "success"
    return "db connection error"

def get_users():
    db = threadpool.connect()
    if db is not None:
        cursor =  db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT user_name, email, auth FROM user WHERE blocked=0;"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            db.close()
            return results
        except MySQLdb.Error as e:
            logging.error("Error %d: %s", e.args[0], e.args[1])
    return "db connection error"

def get_blocked_users():
    db = threadpool.connect()
    if db is not None:
        cursor =  db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT user_name, email, auth FROM user WHERE blocked=1;"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            db.close()
            return results
        except MySQLdb.Error as e:
            logging.error("Error %d: %s", e.args[0], e.args[1])
    return "db connection error"

def block_user(username):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE user SET blocked=%s WHERE user_name=%s;"
        try:
            cursor.execute(sql, (1, username))
            cursor.close()
            db.commit()
            db.close()
        except MySQLdb.Error as e:
            db.rollback()
            logging.error("Error %d: %s", e.args[0], e.args[1])
        return "success"
    return "db connection error"

def unblock_user(username):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE user SET blocked=%s WHERE user_name=%s;"
        try:
            cursor.execute(sql, (0, username))
            cursor.close()
            db.commit()
            db.close()
        except MySQLdb.Error as e:
            db.rollback()
            logging.error("Error %d: %s", e.args[0], e.args[1])
        return "success"
    return "db connection error"

def get_signup_requests():
    db = threadpool.connect()
    if db is not None:
        cursor =  db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT user_name, email FROM user WHERE approved=0;"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            db.close()
            return results
        except MySQLdb.Error as e:
            logging.error("Error %d: %s", e.args[0], e.args[1])
    return "db connection error"

def approve_user(username):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE user SET approved=%s WHERE user_name=%s;"
        try:
            cursor.execute(sql, (1, username))
            cursor.close()
            db.commit()
            db.close()
        except MySQLdb.Error as e:
            db.rollback()
            logging.error("Error %d: %s", e.args[0], e.args[1])
        return "success"
    return "db connection error"

def get_heavy_users():
    db = threadpool.connect()
    if db is not None:
        cursor =  db.cursor(MySQLdb.cursors.DictCursor)
        MONTH = 60 * 60 * 24 * 30
        sql = "SELECT user_name, sum(size) AS size FROM download WHERE completed_time > unix_timestamp(now()) - %s GROUP BY user_name ORDER BY size DESC LIMIT 10;" % MONTH
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            db.close()
            return results
        except MySQLdb.Error as e:
            logging.error("Error %d: %s", e.args[0], e.args[1])
    return "db connection error"

def check_if_bandwidth_exceeded(username):
    db = threadpool.connect()
    if db is not None:
        cursor =  db.cursor(MySQLdb.cursors.DictCursor)
        MONTH = 60 * 60 * 24 * 30
        sql = "SELECT sum(size) AS sum FROM download WHERE completed_time > unix_timestamp(now()) - %s AND user_name=%s;"
        try:
            cursor.execute(sql, (MONTH, username))
            result = cursor.fetchone()
            cursor.close()
            db.close()
            if result['sum'] == None:
                return False
            elif result['sum'] > conf['max_bandwidth']:
                return True
            else:
                return False
            return result
        except MySQLdb.Error as e:
            logging.error("Error %d: %s", e.args[0], e.args[1])
    return "db connection error"
