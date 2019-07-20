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
        if db is not None:
            cursor = db.cursor()
            query = "INSERT INTO folder (name, user_id, parent_id) VALUES(%s, %s, %s);"
            try:
                cursor.execute(query, (name, user_id, parent_id))
                db.commit()
            except MySQLdb.Error as e:
                db.rollback()
                return e
            return 'success'
        return 'db connection error'

    def delete(self, id):
        db = threadpool.connect()
        if db is not None:
            cursor = db.cursor()
            query = "DELETE FROM folder WHERE id=%s OR parent_id=%s;"
            try:
                cursor.execute(query, (id, id))
                db.commit()
            except MySQLdb.Error as e:
                db.rollback()
                return e
            return 'success'
        return 'db connection error'

    def update(self, name, id):
        db = threadpool.connect()
        if db is not None:
            cursor = db.cursor()
            query = "UPDATE folder SET name=%s WHERE id=%s;"
            try:
                cursor.execute(query, (name, id))
                db.commit()
            except MySQLdb.Error as e:
                db.rollback()
                return e
            return 'success'
        return 'db connection error'

    def get(self, id):
        db = threadpool.connect()
        if db is not None:
            cursor = db.cursor()
            sql = "SELECT id, name FROM folder WHERE id=%s;"
            try:
                cursor.execute(sql, (id))
                results = cursor.fetchall()
                db.close()
                return results
            except MySQLdb.Error as e:
                return e
        return 'db connection error'

    def get_all(self, id):
        db = threadpool.connect()
        if db is not None:
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
        return 'db connection error'



############################### File class ###################################


class File(EntityInterface):

    def create(name, user_id, parent_id):
        db = threadpool.connect()
        if db is not None:
            cursor = db.cursor()
            query = "INSERT INTO file (name, user_id, parent_id) VALUES(%s, %s, %s);"
            try:
                cursor.execute(query, (name, user_id, parent_id))
                db.commit()
            except MySQLdb.Error as e:
                db.rollback()
                return e
            return 'success'
        return 'db connection error'

    def delete(id):
        db = threadpool.connect()
        if db is not None:
            cursor = db.cursor()
            query = "DELETE FROM file WHERE id=%s OR parent_id=%s;"
            try:
                cursor.execute(query, (id, id))
                db.commit()
            except MySQLdb.Error as e:
                db.rollback()
                return e
            return 'success'
        return 'db connection error'

    def update(name, id):
        db = threadpool.connect()
        if db is not None:
            cursor = db.cursor()
            query = "UPDATE file SET name=%s WHERE id=%s;"
            try:
                cursor.execute(query, (name, id))
                db.commit()
            except MySQLdb.Error as e:
                db.rollback()
                return e
            return 'success'
        return 'db connection error'

    def get(id):
        db = threadpool.connect()
        if db is not None:
            cursor = db.cursor()
            sql = "SELECT id, name FROM file WHERE id=%s;"
            try:
                cursor.execute(sql, (id))
                results = cursor.fetchall()
                db.close()
                return results
            except MySQLdb.Error as e:
                return e
        return 'db connection error'
