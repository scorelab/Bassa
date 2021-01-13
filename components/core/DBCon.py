import MySQLdb
import os

_db=None

def get_db_con () :
    global _db
    if _db==None:
        try:
          _db=MySQLdb.connect("db", os.environ.get('BASSA_DB_USERNAME'), os.environ.get('BASSA_DB_PASSWORD'), os.environ.get('BASSA_DB_NAME'))
          return _db

        except Exception as e:
            print("DATABASE FAILED TO CONNECT: " + str(e))
            #Tests to see if it's a common error. If it is links user to stackoverflow post
            if str(e) == r"""(2059, "Authentication plugin 'caching_sha2_password' cannot be loaded: The specified module could not be found.\r\n")""":
               print("")
               print("Refer to: https://stackoverflow.com/questions/49194719/authentication-plugin-caching-sha2-password-cannot-be-loaded")

            return None
    else:
        return _db

def close_db_con () :
    if _db!=None:
        _db.close()
