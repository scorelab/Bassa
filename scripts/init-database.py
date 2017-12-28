#!/usr/bin/env python

import yaml
import sqlalchemy
import os
import getpass

configs = 'configurations'
path = 'root_path'


def retreive_values():
    global path
    global configs
    path= os.path.abspath(os.path.join(os.path.join(__file__,os.pardir),os.pardir))
    stream = open(path+"/bassa.yml", "r")
    configs = yaml.load(stream)


def create_database():
    root_password = getpass.getpass(prompt = 'Enter root password:')
    param = configs['database']['database_type']+'://root:'+root_password+'@'+configs['database']['database_ip']
    engine = sqlalchemy.create_engine(param)
    engine.execute("CREATE DATABASE IF NOT EXISTS " + configs['database']['database_name'])
    engine.execute("CREATE USER "+configs['database']['database_user_username']+"@"+configs['database']['database_ip']+" IDENTIFIED BY " + configs['database']['database_user_password'])
    engine.execute("GRANT INSERT, UPDATE, SELECT, DELETE ON "+configs['database']['database_name']+".* TO "+configs['database']['database_user_username']+"@"+configs['database']['database_ip'])
    engine.execute("FLUSH PRIVILEGES")


def import_SQL():
    connection_url = configs['database']['database_type']+'://'+configs['database']['database_user_username']+':'+configs['database']['database_user_password']+'@'+configs['database']['database_ip']+'/'+configs['database']['database_name']
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
    print "Database (" + configs['database']['database_name'] + ") is now successfuly setup"

