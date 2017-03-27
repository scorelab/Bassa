import MySQLdb
from ConfReader import get_conf_reader

conf = get_conf_reader("main.conf")

_db=None

def get_db_con () :
    global _db
    if _db==None:
        try:
            _db=MySQLdb.connect("localhost", conf['db']['u_name'], conf['db']['u_pass'], "Bassa" )
            return _db
        except:
            return None
    else:
        return _db

def close_db_con () :
    if _db!=None:
        _db.close()
