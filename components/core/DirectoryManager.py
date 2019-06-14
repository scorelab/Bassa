from Models import Workspace, Project, Folder
from DBCon import *
from ConfReader import get_conf_reader
import sqlalchemy.pool as pool

conf = get_conf_reader("dl.conf")

threadpool = pool.QueuePool(get_db_con, max_overflow=10, pool_size=20)

def get_all_workspaces(user_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT name FROM workspace WHERE user_id=%d;"
        try:
            cursor.execute(sql, (user_id))
            db.commit()
        except MySQLdb.error as e:
            db.rollback()
            return e[1]
        return 'success'
    return 'db connection error'

def get_workspace_by_id(user_id, workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT name FROM workspace WHERE id=%d AND user_id=%d;"
        try:
            cursor.execute(sql, (workspace_id, user_id))
            db.commit()
        except MySQLdb.error as e:
            db.rollback()
            return e[1]
        return 'success'
    return 'db connection error'

def create_workspace(name, user_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT into workspace VALUES(%s, %d);"
        try:
            cursor.execute(sql, (name, user_id))
            db.commit()
        except MySQLdb.error as e:
            db.rollback()
            return e[1]
        return 'success'
    return 'db connection error'

def update_workspace(name, user_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE workspace SET name=%s where user_id=%d;"
        try:
            cursor.execute(sql, (name, user_id))
            db.commit()
        except MySQLdb.error as e:
            db.rollback()
            return e[1]
        return 'success'
    return 'db connection error'