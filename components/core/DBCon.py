import MySQLdb
import os

_db=None

def get_db_con () :
    global _db
    if _db==None:
        try:
            _db=MySQLdb.connect("db", os.environ.get('BASSA_DB_USERNAME'), os.environ.get('BASSA_DB_PASSWORD'), os.environ.get('BASSA_DB_NAME'))
            return _db
        except:
            return None
    else:
        return _db

def close_db_con () :
    if _db!=None:
        _db.close()
