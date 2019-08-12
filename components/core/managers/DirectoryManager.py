from Models import EntityInterface
from DBCon import *
# from utils.entity_utils import *
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


    def delete(self, id, user_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "DELETE FROM folder WHERE id=%s AND user_id=%s;"
        try:
            cursor.execute(query, (id, user_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def update(self, new_name, id, user_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "UPDATE folder SET name=%s WHERE id=%s AND user_id=%s;"
        try:
            cursor.execute(query, (new_name, id, user_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def get(self, id, user_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "SELECT id,name FROM folder WHERE id=%s AND user_id=%s;"
        try:
            cursor.execute(query, (id, user_id))
            db_result = cursor.fetchall()
            db.close()

            def serialize_results(q_res):
                result = list()
                for elem in q_res:
                    obj = dict()
                    obj['type'] = 'fr'
                    obj['name'] = elem[1]
                    obj['id'] = elem[0]
                    result.append(obj)
                return result

            return serialize_results(db_result)
        except MySQLdb.Error as e:
            return str(e)


    def move(self, id, user_id, parent_name):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = 'UPDATE folder SET parent_id = ( SELECT id FROM ( SELECT * FROM folder ) AS folder WHERE name=%s AND user_id=%s ) WHERE id=%s AND user_id=%s;'
        try:
            cursor.execute(query, (parent_name, user_id, id, user_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def get_all(self, user_id, id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        folder_query = "SELECT id,name FROM folder WHERE parent_id=%s;"
        file_query = "SELECT id,name FROM file WHERE parent_id=%s;"
        try:
            cursor.execute(folder_query, (id))
            folder_result = cursor.fetchall()
            cursor.execute(file_query, (id))
            file_result = cursor.fetchall()
            db.close()

            def serialize_results(folder, file):
                result = list()
                folder_list = list()
                file_list = list()
                for tup in folder:
                    folder_obj = dict()
                    folder_obj['id'] = tup[0]
                    folder_obj['name'] = tup[1]
                    folder_list.append(folder_obj)
                for tup in file:
                    file_obj = dict()
                    file_obj['id'] = tup[0]
                    file_obj['name'] = tup[1]
                    file_list.append(file_obj)

                folder_dict = dict()
                folder_dict['type'] = 'fr'
                folder_dict['items'] = folder_list

                file_dict = dict()
                file_dict['type'] = 'fl'
                file_dict['items'] = file_list

                result.append(folder_dict)
                result.append(file_dict)
                return result

            results = serialize_results(folder_result, file_result)
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


    def delete(self, id, user_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "DELETE FROM file WHERE id=%s AND user_id=%s;"
        try:
            cursor.execute(query, (id, user_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def update(self, new_name, id, user_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = "UPDATE file SET name=%s WHERE id=%s AND user_id=%s;"
        try:
            cursor.execute(query, (new_name, id, user_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'


    def get(self, id, user_id):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        sql = "SELECT id,name FROM file WHERE id=%s AND user_id=%s;"
        try:
            cursor.execute(sql, (id, user_id))
            db_result = cursor.fetchall()
            db.close()

            def serialize_results(q_res):
                result = list()
                for elem in q_res:
                    obj = dict()
                    obj['type'] = 'fr'
                    obj['name'] = elem[1]
                    obj['id'] = elem[0]
                    result.append(obj)
                return result

            return serialize_results(db_result)
        except MySQLdb.Error as e:
            return str(e)


    def move(self, id, user_id, parent_name):
        db = threadpool.connect()
        if db is None:
            return 'db connection error'
        cursor = db.cursor()
        query = 'UPDATE file SET parent_id = ( SELECT id FROM folder WHERE name=%s AND user_id=%s ) WHERE id=%s AND user_id=%s;'
        try:
            cursor.execute(query, (parent_name, user_id, id, user_id))
            db.commit()
        except MySQLdb.Error as e:
            db.rollback()
            return str(e)
        return 'success'
