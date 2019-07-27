from Models import EntityInterface
from DBCon import *
import sqlalchemy.pool as pool

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
            return str(e)
        return 'success'


    def delete(self, user_id, name):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "DELETE FROM folder WHERE user_id=%s AND name=%s;"
        try:
            cursor.execute(query, (user_id, name))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def update(self, new_name, name, user_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "UPDATE folder SET name=%s WHERE user_id=%s AND name=%s;"
        try:
            cursor.execute(query, (new_name, user_id, name))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def get(self, name, user_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "SELECT name FROM folder WHERE user_id=%s AND name=%s;"
        try:
            cursor.execute(query, (user_id, name))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return str(e)


    def move(self, name, user_id, parent_name):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = 'UPDATE folder SET parent_id = ( SELECT id FROM folder WHERE name=%s AND user_id=%s ) WHERE user_id=%s AND name=%s;'
        try:
            cursor.execute(query, (parent_name, user_id, user_id, name))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def get_all(self, user_id, name):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        folder_query = "SELECT name FROM folder WHERE parent_id = ( SELECT id FROM folder WHERE name=%s AND user_id=%s );"
        file_query = "SELECT name FROM file WHERE parent_id = ( SELECT id FROM folder WHERE name=%s AND user_id=%s );"
        try:
            cursor.execute(folder_query, (name, user_id))
            cursor.execute(file_query, (name, user_id))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return str(e)


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
            return str(e)
        return 'success'


    def delete(self, user_id, name):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "DELETE FROM file WHERE user_id=%s AND name=%s;"
        try:
            cursor.execute(query, (user_id, name))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def update(self, new_name, name, user_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "UPDATE file SET name=%s WHERE user_id=%s AND name=%s;"
        try:
            cursor.execute(query, (new_name, user_id, name))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def get(self, name, user_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        sql = "SELECT name FROM file WHERE user_id=%s AND name=%s;"
        try:
            cursor.execute(sql, (user_id, name))
            results = cursor.fetchall()
            db.close()
            return results
        except MySQLdb.Error as e:
            return str(e)


    def move(self, name, user_id, parent_name):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = 'UPDATE file SET parent_id = ( SELECT id FROM folder WHERE name=%s AND user_id=%s ) WHERE user_id=%s AND name=%s;'
        try:
            cursor.execute(query, (parent_name, user_id, user_id, name))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'
