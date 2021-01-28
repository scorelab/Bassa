import MySQLdb
from ConfReader import get_conf_reader
import os

_db=None
db_conf = get_conf_reader("db.config.json")

def get_db_con () :
    global _db
    if _db==None:
        try:
            _db=MySQLdb.connect(host=db_conf["BASSA_HOST"], user=db_conf["BASSA_DB_USERNAME"], passwd=db_conf["BASSA_DB_PASSWORD"],db=db_conf["BASSA_DB_NAME"])
            return _db
        except:
            return None
    else:
        return _db

def close_db_con () :
    if _db!=None:
        _db.close()
