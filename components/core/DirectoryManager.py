from Models import Workspace, Project, Folder
from DBCon import *
from ConfReader import get_conf_reader
import sqlalchemy.pool as pool

conf = get_conf_reader("dl.conf")

threadpool = pool.QueuePool(get_db_con, max_overflow=10, pool_size=20)


##################### workspace helper functions ######################

def get_workspaces(user_id):
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

def get_workspace_by_id(workspace_id, user_id):
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

def update_workspace(name, id, user_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE workspace SET name=%s WHERE id=%d AND user_id=%d;"
        try:
            cursor.execute(sql, (name, id, user_id))
            db.commit()
        except MySQLdb.error as e:
            db.rollback()
            return e[1]
        return 'success'
    return 'db connection error'


##################### project helper functions ######################

def get_projects(workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT name FROM project WHERE workspace_id=%d;"
        try:
            cursor.execute(sql, (workspace_id))
            db.commit()
        except MySQLdb.error as e:
            db.rollback()
            return e[1]
        return 'success'
    return 'db connection error'

def get_project_by_id(project_id, workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT name FROM project WHERE id=%d AND workspace_id=%d;"
        try:
            cursor.execute(sql, (project_id, workspace_id))
            db.commit()
        except MySQLdb.error as e:
            db.rollback()
            return e[1]
        return 'success'
    return 'db connection error'

def create_project(name, workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT into project VALUES(%s, %d);"
        try:
            cursor.execute(sql, (name, workspace_id))
            db.commit()
        except MySQLdb.error as e:
            db.rollback()
            return e[1]
        return 'success'
    return 'db connection error'

def update_project(name, id, workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE project SET name=%s where id=%d AND workspace_id=%d;"
        try:
            cursor.execute(sql, (name, id, workspace_id))
            db.commit()
        except MySQLdb.error as e:
            db.rollback()
            return e[1]
        return 'success'
    return 'db connection error'
