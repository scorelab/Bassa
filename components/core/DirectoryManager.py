from Models import EntityInterface
from DBCon import *
from ConfReader import get_conf_reader
import sqlalchemy.pool as pool

conf = get_conf_reader("dl.conf")

threadpool = pool.QueuePool(get_db_con, max_overflow=10, pool_size=20)


############################### Folder class ###################################

class Folder(EntityInterface):

    def create(self, name, user_id, parent_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "INSERT INTO folder (name, user_id, parent_id) VALUES(%s, %s, %s);"
        try:
            cursor.execute(query, (name, user_id, parent_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'


    def delete(self, id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "DELETE FROM folder WHERE id=%s OR parent_id=%s;"
        try:
            cursor.execute(query, (id, id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'


    def update(self, name, id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "UPDATE folder SET name=%s WHERE id=%s;"
        try:
            cursor.execute(query, (name, id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'


    def get(self, id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "SELECT id, name FROM folder WHERE id=%s;"
        try:
            cursor.execute(query, (id))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return e


    def move(self, id, parent_name):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = 'UPDATE folder SET parent_id = ( SELECT id FROM folder WHERE name=%s ) where id=%s;'
        try:
            cursor.execute(query, (parent_name, id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def get_all(self, id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        folder_query = "SELECT id, name FROM folder WHERE parent_id=%s;"
        file_query = "SELECT id, name FROM file WHERE parent_id=%s;"
        try:
            cursor.execute(folder_query, (id))
            cursor.execute(file_query, (id))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return e


############################### File class ###################################


class File(EntityInterface):

    def create(self, name, user_id, parent_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "INSERT INTO file (name, user_id, parent_id) VALUES(%s, %s, %s);"
        try:
            cursor.execute(query, (name, user_id, parent_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'


    def delete(self, id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "DELETE FROM file WHERE id=%s OR parent_id=%s;"
        try:
            cursor.execute(query, (id, id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'


    def update(self, name, id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "UPDATE file SET name=%s WHERE id=%s;"
        try:
            cursor.execute(query, (name, id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return e
        return 'success'


    def get(self, id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        sql = "SELECT id, name FROM file WHERE id=%s;"
        try:
            cursor.execute(sql, (id))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return e


    def move(self, id, parent_name):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = 'UPDATE file SET parent_id = ( SELECT id FROM folder WHERE name=%s ) where id=%s;'
        try:
            cursor.execute(query, (parent_name, id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e) 
        return 'success'
