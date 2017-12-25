#!/bin/bash
read -p " database_type: " database_type;
read -p "database_port: " database_port;
read -p "database_ip: " database_ip;
read -p "database_name: " database_name;
read -p "database_user_username: " database_user_username;
read -p "databse_user_password: " databse_user_password;
echo "database:" > ../bassa.yml;
echo "database_type: $database_type" >> ../bassa.yml;
echo "database_port: $database_port" >> ../bassa.yml;
echo "database_ip: $database_ip" >> ../bassa.yml;
echo "database_name: $database_name" >> ../bassa.yml;
echo "database_user_username: $database_user_username" >> ../bassa.yml;
echo "database_user_password: $databse_user_password" >> ../bassa.yml;
echo "Entered Credentials Have Been Stored";
