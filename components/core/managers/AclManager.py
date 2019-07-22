from DBCon import *
import sqlalchemy.pool as pool

threadpool = pool.QueuePool(get_db_con, max_overflow=10, pool_size=20)


def get_access(id, user_id, entity):
    db = threadpool.connect()
    if db is None:
        return 'db connection error'
    cursor = db.cursor()
    query = "SELECT access FROM acl WHERE entity_id=%s and user_id=%s and entity_type=%s;"
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
    query = "INSERT INTO acl (user_id, entity_type, entity_id, access) SELECT id, %s, %s, %s FROM user WHERE user_name=%s;"
    try:
        cursor.execute(query, (entity, id, access, user_name))
        db.commit()
    except MySQLdb.Error as e:
        db.rollback()
        return str(e)
    return 'success'