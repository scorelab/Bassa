from DBCon import *
import sqlalchemy.pool as pool

threadpool = pool.QueuePool(get_db_con, max_overflow=10, pool_size=20)

def get_notif(user_id):
    db = threadpool.connect()
    if db is None:
        return 'db connection error'
    cursor = db.cursor()
    query = "SELECT notif FROM notifications WHERE user_id=%s;"
    try:
        cursor.execute(query, (user_id))
        results = cursor.fetchall()
        db.close()
        return results
    except MySQLdb.Error as e:
        return str(e)

def post_notif(username, notif):
    db = threadpool.connect()
    if db is None:
        return 'db connection error'
    cursor = db.cursor()
    query = "INSERT INTO notifications (user_id, notif) SELECT id, %s FROM user WHERE user_name=%s;"
    try:
        cursor.execute(query, (notif, username))
        db.commit()
    except MySQLdb.Error as e:
        db.rollback()
        return str(e)
    return 'success'