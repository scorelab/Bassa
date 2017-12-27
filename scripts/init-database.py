#!/usr/bin/env python

import yaml, sqlalchemy, MySQLdb

stream = open("../.config/bassa/config.yml", "r")
docs = yaml.load_all(stream)
values = list()
for doc in docs:
    for k,v in doc.items():
        for m,n in v.items():
		values.append(n)
dbtype=values[5]
dbusername=values[0]
dbpass=values[4]
ip=values[2]
# db=MySQLdb.connect(host="localhost", user="bassaman",passwd="s57d46857f968t79pho")
# db1=db.cursor()
# db1.execute('Create database test100')
engine = sqlalchemy.create_engine(dbtype+'://'+dbusername+':'+dbpass+'@'+ip)
engine.execute("CREATE DATABASE IF NOT EXISTS " + values[3])
engine = sqlalchemy.create_engine(dbtype+'://'+dbusername+':'+dbpass+'@'+ip+'/'+values[3])
fd = open("../Bassa.sql",'r')
sqlFile = fd.read()
fd.close()
sqlCommands=sqlFile.split(';')
for command in sqlCommands:
	with engine.connect() as con:
		rs = con.execute(command+';')
