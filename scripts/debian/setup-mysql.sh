#!/bin/bash
mysql_root_password='s57d46857f968t79pho';
port="3006";
echo "";
echo "Installing MySQL on Debian based Linux"
echo "";
sudo apt-get update;
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password '$mysql_root_password;
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password '$mysql_root_password;
sudo apt-get -y install mysql-server;
sudo sed -i "s/port.*/port = $port/" /etc/mysql/mysql.conf.d/mysqld.cnf;
sudo service mysql stop;
sudo service mysql start;
echo "";
echo "MySQL Installed Successfully";
