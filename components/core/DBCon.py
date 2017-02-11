import pymysql.cursors

_db=None

def get_db_con () :
    global _db
    if _db==None:
        try:
            _db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='Bassa',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            return _db
        except:
            return None
    else:
        return _db

def close_db_con () :
    if _db!=None:
        _db.close()
