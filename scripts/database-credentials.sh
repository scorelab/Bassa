#!/bin/bash
port="3306";
ip="127.0.0.1";
name="bassa";
while [[ -z "$DBTYPE" ]]
do
    read -p "Database type: " DBTYPE;
done
read -p "Database port [$port]: " DBPORT;
read -p "Database ip [$ip]: " DBIP;
read -p "Database name [$name]: " DBNAME;
while [[ -z "$DBUSERNAME" ]]
do
    read -p "Database username: " DBUSERNAME;
done
while [[ -z "$DBPASSWORD" ]]
do
    read -p "Database password: " -s DBPASSWORD && echo "";
done
DBPORT=${DBPORT:-$port};
DBIP=${DBIP:-$ip};
DBNAME=${DBNAME:-$name};
echo "database:" > ../bassa.yml;
echo "    database_type: $DBTYPE" >> ../bassa.yml;
echo "    database_port: $DBPORT" >> ../bassa.yml;
echo "    database_ip: $DBIP" >> ../bassa.yml;
echo "    database_name: $DBNAME" >> ../bassa.yml;
echo "    database_user_username: $DBUSERNAME" >> ../bassa.yml;
echo "    database_user_password: $DBPASSWORD" >> ../bassa.yml;
echo "Credentials Stored!";
