#!/usr/bin/env python

import yaml
import sqlalchemy
import os
import getpass

configs = ''
path = ''


def retreive_values():
    global path
    global configs
    path= os.path.abspath(os.path.join(os.path.join(__file__,os.pardir),os.pardir))
    stream = open(path+"/bassa.yml", "r")
    configs = yaml.safe_load(stream)


def create_database():
    root_password = os.environ['MYSQL_ROOT_PASSWORD']
    if not root_password:
        root_password = getpass.getpass(prompt = 'Enter root password:')
        os.environ['MYSQL_ROOT_PASSWORD'] = root_password
    connection_url = configs['database']['database_type']+'://root:'+os.environ['MYSQL_ROOT_PASSWORD']+'@'+configs['database']['database_ip']
    engine = sqlalchemy.create_engine(connection_url)
    engine.execute("CREATE DATABASE IF NOT EXISTS " + configs['database']['database_name'])
    engine.execute("CREATE USER "+configs['database']['database_user_username']+"@"+configs['database']['database_ip']+" IDENTIFIED BY " + configs['database']['database_user_password'])
    engine.execute("GRANT INSERT, UPDATE, SELECT, DELETE ON "+configs['database']['database_name']+".* TO "+configs['database']['database_user_username']+"@"+configs['database']['database_ip'])


def import_sql():
    connection_url = configs['database']['database_type']+'://'+configs['database']['database_user_username']+':'+configs['database']['database_user_password']+'@'+configs['database']['database_ip']+'/'+configs['database']['database_name']
    engine = sqlalchemy.create_engine(connection_url)
    fd = open(path+"/Bassa.sql", 'r')
    sql_File = fd.read()
    fd.close()
    sqlCommands = sql_File.split(';')
    for command in sqlCommands:
        try:
            with engine.connect() as con:
                con.execute(command+';')
        except Exception as exception:
            print('init-database: exception: %s ', exception)

if __name__ == "__main__":
    retreive_values()
    create_database()
    import_sql()
    print "Database (" + configs['database']['database_name'] + ") is now successfuly setup"

