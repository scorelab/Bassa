from Models import Download
from DBCon import *
import time


def add_download(download):
    db = get_db_con()
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT into download(link, user_name, added_time) VALUES(%s, %s, %s);"
        try:
            cursor.execute(sql, (download.link, download.userName, time.time()))
            db.commit()
        except MySQLdb.Error, e:
            db.rollback()
            return e[1]
        return "success"
    return "db connection error"