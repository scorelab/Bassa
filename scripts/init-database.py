#!/usr/bin/env python

import yaml
import sqlalchemy
import MySQLdb

values = list()


def retreiveValues():
    stream = open("../.config/bassa/config.yml", "r")
    docs = yaml.load_all(stream)
    global values
    for doc in docs:
        for k, v in doc.items():
            for m, n in v.items():
                values.append(n)


def createDatabase():
    param = values[5]+'://'+values[0]+':'+values[4]+'@'+values[2]
    engine = sqlalchemy.create_engine(param)
    engine.execute("CREATE DATABASE IF NOT EXISTS " + values[3])


def importSQL():
    param = values[5]+'://'+values[0]+':'+values[4]+'@'+values[2]+'/'+values[3]
    engine = sqlalchemy.create_engine(param)
    fd = open("../Bassa.sql", 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    for command in sqlCommands:
        try:
            with engine.connect() as con:
                con.execute(command+';')
        except:
            error = 1
retreiveValues()
createDatabase()
importSQL()
print "Database (" + values[3] + ") is now successfuly setup"

