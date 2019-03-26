import MySQLdb
import os

_db=None

def get_db_con () :
    global _db
    print("###")
    if _db==None:
        try:
            _db=MySQLdb.connect(host="localhost", user="root", passwd="password",db= "Bassa")
            return _db
        except:
            return None
    else:
        return _db

def close_db_con () :
    if _db!=None:
        _db.close()
