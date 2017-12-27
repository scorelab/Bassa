#!/usr/bin/env python

import yaml
import sqlalchemy
import os

values = 'configurations'
path = 'root_path'


def retreive_values():
    global path
    path= os.path.abspath(os.path.join(os.path.join(__file__,os.pardir),os.pardir))
    stream = open(path+"/bassa.yml", "r")
    configs = yaml.load(stream)
    global values
    values = configs


def create_database():
    param = values['database']['database_type']+'://'+values['database']['database_user_username']+':'+values['database']['database_user_password']+'@'+values['database']['database_ip']
    try:
        engine = sqlalchemy.create_engine(param)
	engine.execute("CREATE DATABASE IF NOT EXISTS " + values['database']['database_name'])
    except:
        param = values['database']['database_type']+'://root:'+values['database']['database_user_password']+'@'+values['database']['database_ip']
	engine = sqlalchemy.create_engine(param)
	engine.execute("CREATE DATABASE IF NOT EXISTS " + values['database']['database_name'])
	engine.execute("GRANT ALL PRIVILEGES ON "+values['database']['database_name']+" TO "+values['database']['database_user_username']+"@"+values['database']['database_ip']+"WITH GRANT OPTION;")


def import_SQL():
    param = values['database']['database_type']+'://'+values['database']['database_user_username']+':'+values['database']['database_user_password']+'@'+values['database']['database_ip']+'/'+values['database']['database_name']
    fd = open(path+"/Bassa.sql", 'r')
    sql_File = fd.read()
    fd.close()
    sqlCommands = sql_File.split(';')
    for command in sqlCommands:
        try:
            with engine.connect() as con:
                con.execute(command+';')
        except:
            pass


if __name__ == "__main__":
    retreive_values()
    create_database()
    import_SQL()
    print "Database (" + values['database']['database_name'] + ") is now successfuly setup"
