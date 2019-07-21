from DBCon import *
from ConfReader import get_conf_reader
import sqlalchemy.pool as pool

conf = get_conf_reader("dl.conf")

threadpool = pool.QueuePool(get_db_con, max_overflow=10, pool_size=20)

def check(id, user_id, entity):
    db = threadpool.connect()
    if db is None:
        return 'db connection error'
    cursor = db.cursor()
    query = "SELECT access FROM acl WHERE id=%s and user_id=%s and entity_type=%;"
    try:
        cursor.execute(query, (id))
        results = cursor.fetchall()
        db.close()
        return results
    except MySQLdb.Error as e:
        return e

def grant(id, user_id, entity, access):
    db = threadpool.connect()
    if db is None:
        return 'db connection error'
    cursor = db.cursor()
    query = "INSERT INTO acl (user_id, entity_type, entity_id, access) VALUES (%s, %s, %s, %s);"
    try:
        cursor.execute(query, (user_id, entity, id, access))
        db.commit()
    except MySQLdb.Error as e:
        db.rollback()
        return e
    return 'success'