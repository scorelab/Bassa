import MySQLdb
from ConfReader import get_conf_reader

mainconf = get_conf_reader("dl.conf")

_db=None

def get_db_con () :
    global _db
    if _db==None:
        try:
            _db=MySQLdb.connect(mainconf['database']['host'], mainconf['database']['user'], mainconf['database']['password'], mainconf['database']['dbName'] )
            return _db
        except:
            return None
    else:
        return _db

def close_db_con () :
    if _db!=None:
        _db.close()


