import MySQLdb
from ConfReader import get_conf_reader
import os

_db=None
dbConf = get_conf_reader("db.config.json")

def get_db_con () :
    global _db
    if _db==None:
        try:
            _db=MySQLdb.connect(host=dbConf["BASSA_HOST"], user=dbConf["BASSA_DB_USERNAME"], passwd=dbConf["BASSA_DB_PASSWORD"],db=dbConf["BASSA_DB_NAME"])
            return _db
        except:
            return None
    else:
        return _db

def close_db_con () :
    if _db!=None:
        _db.close()
