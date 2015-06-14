from Models import User
from DBCon import *


def user_login(username, password):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT * FROM user WHERE user_name=%s AND password=MD5(%s) AND blocked=0;"
        cursor.execute(sql, (username, password))
        data = cursor.fetchone()
        if data == None:
            return False
        else:
            return True


def check_user_name(username):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT * FROM user WHERE user_name=%s;"
        cursor.execute(sql, (username))
        data = cursor.fetchone()
        if data == None:
            return False
        else:
            return True


def get_user(username):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT * FROM user WHERE user_name=%s and blocked=0;"
        cursor.execute(sql, (username))
        data = cursor.fetchone()
        if data == None:
            return None
        else:
            return User(data['user_name'], data['password'], data['auth'], data['email'])


def add_user(user):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT into user VALUES(%s, MD5(%s), %s, %s, 0);"
        try:
            cursor.execute(sql, (user.userName, user.password, user.auth, user.email))
            db.commit()
        except MySQLdb.Error, e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"


def remove_user(username):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "DELETE from user WHERE user_name=%s;"
        try:
            cursor.execute(sql, (username))
            db.commit()
        except MySQLdb.Error, e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"


def update_user(user, username):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE user SET user_name=%s, auth=%s, email=%s WHERE user_name=%s;"
        try:
            cursor.execute(sql, (user.userName, user.auth, user.email, username))
            db.commit()
        except MySQLdb.Error, e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"

def get_users():
    db = get_db_con()
    if db is not None:
        cursor =  db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT user_name, email, auth FROM user WHERE blocked=0;"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except MySQLdb.Error, e:
            return e[1]
    return "db connection error"

def get_blocked_users():
    db = get_db_con()
    if db is not None:
        cursor =  db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT user_name, email, auth FROM user WHERE blocked=1;"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except MySQLdb.Error, e:
            return e[1]
    return "db connection error"

def block_user(username):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE user SET blocked=%s WHERE user_name=%s;"
        try:
            cursor.execute(sql, (1, username))
            db.commit()
        except MySQLdb.Error, e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"

def unblock_user(username):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE user SET blocked=%s WHERE user_name=%s;"
        try:
            cursor.execute(sql, (0, username))
            db.commit()
        except MySQLdb.Error, e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"
