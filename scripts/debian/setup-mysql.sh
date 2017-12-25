#!/bin/bash
mysql_root_password='s57d46857f968t79pho';
bassa_db_name='bassa'
bassa_user_name='bassa'
bassa_user_password='678yU8O7T87ihu7HU9797U'
echo "";
echo "Installing MySQL on Debian based Linux"
echo "";
sudo apt-get update;
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password '$mysql_root_password;
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password '$mysql_root_password;
sudo apt-get -y install mysql-server;
echo "";
echo "MySQL Installed Successfully";
