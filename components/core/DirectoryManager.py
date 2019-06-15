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
        sql = "SELECT id, name FROM workspace WHERE user_id=%s;"
        try:
            cursor.execute(sql, (user_id))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return e
    return 'db connection error'

def get_workspace_by_id(workspace_id, user_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT id, name FROM workspace WHERE id=%s AND user_id=%s;"
        try:
            cursor.execute(sql, (workspace_id, user_id))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return e
    return 'db connection error'

def create_workspace(name, user_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT INTO workspace (name, user_id) VALUES (%s, %s);"
        try:
            cursor.execute(sql, (name, user_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'
    return 'db connection error'

def update_workspace(name, id, user_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE workspace SET name=%s WHERE id=%s AND user_id=%s;"
        try:
            cursor.execute(sql, (name, id, user_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'
    return 'db connection error'


##################### project helper functions ######################

def get_projects(workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT name FROM project WHERE workspace_id=%s;"
        try:
            cursor.execute(sql, (workspace_id))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return e
    return 'db connection error'

def get_project_by_id(project_id, workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT name FROM project WHERE id=%s AND workspace_id=%s;"
        try:
            cursor.execute(sql, (project_id, workspace_id))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return e
    return 'db connection error'

def create_project(name, workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT INTO project (name, workspace_id) VALUES(%s, %s);"
        try:
            cursor.execute(sql, (name, workspace_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'
    return 'db connection error'

def update_project(name, id, workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE project SET name=%s WHERE id=%s AND workspace_id=%s;"
        try:
            cursor.execute(sql, (name, id, workspace_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'
    return 'db connection error'


##################### folder helper functions ######################

def get_folders(workspace_id, project_id, folder_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT id, name FROM folder WHERE workspace_id=%s AND project_id=%s AND folder_id=%s;"
        try:
            cursor.execute(sql, (workspace_id, project_id, folder_id))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return e
    return 'db connection error'

def get_folder_by_id(id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "SELECT id, name, workspace_id, project_id, folder_id FROM folder WHERE id=%s;"
        try:
            cursor.execute(sql, (id))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return e
    return 'db connection error'

def create_folder(name, folder_id, project_id, workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT INTO folder (name, folder_id, project_id, workspace_id) VALUES(%s, %s, %s, %s);"
        try:
            cursor.execute(sql, (name, folder_id, project_id, workspace_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'
    return 'db connection error'

def update_folder(name, id, folder_id, project_id, workspace_id):
    db = threadpool.connect()
    if db is not None:
        cursor = db.cursor()
        sql = "UPDATE folder SET name=%s where id=%s AND folder_id=%s AND project_id=%s AND workspace_id=%s;"
        try:
            cursor.execute(sql, (name, id, folder_id, project_id, workspace_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'
    return 'db connection error'
