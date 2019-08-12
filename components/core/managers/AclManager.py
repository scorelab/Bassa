from DBCon import *
import sqlalchemy.pool as pool

threadpool = pool.QueuePool(get_db_con, max_overflow=10, pool_size=20)


def get_access(id, user_id, entity):
    db = threadpool.connect()
    if db is None:
        return 'db connection error'
    cursor = db.cursor()
    query = "SELECT access FROM acl WHERE id=%s and user_id=%s and entity_type=%s;"
    try:
        cursor.execute(query, (id, user_id, entity))
        results = cursor.fetchall()
        db.close()
        return results
    except MySQLdb.Error as e:
        return str(e)


def give_access(id, user_name, entity, access):
    db = threadpool.connect()
    if db is None:
        return 'db connection error'
    cursor = db.cursor()
    query = "INSERT INTO acl (user_id, entity_type, id, access) SELECT id, %s, %s, %s FROM user WHERE user_name=%s;"
    try:
        cursor.execute(query, (entity, id, access, user_name))
        db.commit()
    except MySQLdb.Error as e:
        db.rollback()
        return str(e)
    return 'success'


def fetch_shared(user_id):
    db = threadpool.connect()
    if db is None:
        return 'db connection error'
    cursor = db.cursor()
    folder_query = "SELECT id,name,access FROM acl JOIN folder USING (id) WHERE acl.user_id=%s AND acl.entity_type='fr';"
    file_query = "SELECT id,name,access FROM acl JOIN file USING (id) WHERE acl.user_id=%s AND acl.entity_type='fl';"
    try:
        cursor.execute(folder_query, (user_id))
        folder_result = cursor.fetchall()
        cursor.execute(file_query, (user_id))
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
                folder_obj['access'] = tup[2]
                folder_list.append(folder_obj)
            for tup in file:
                file_obj = dict()
                file_obj['id'] = tup[0]
                file_obj['name'] = tup[1]
                file_obj['access'] = tup[2]
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