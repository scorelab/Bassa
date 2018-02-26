#!/bin/bash

echo "Installing pip"
apt-get install -y python3-pip
echo "pip installed"

echo "Installing setuptools"
apt-get install -y python3-setuptools
echo "pip installed"

echo "Installing Aria2"
apt-get install -y aria2
echo "Aria2 installed"

echo "Installing mysql-server"
# apt-get install -y mysql-server
echo "mysql-server installed"

echo "Installing libmysqlclient"
apt-get install libmysqlclient-dev
echo "libmysqlclient installed"

echo "Installing node"
curl -sL https://deb.nodesource.com/setup_6.x | bash -
apt-get install -y nodejs
echo "NodeJS installed"

echo "Installing bower globally"
npm install -g bower
echo "bower installed"

echo "Installing gulp globally"
npm install -g gulp
echo "gulp installed"

# save the directory for further uses
pwd > main_directory.txt

echo "Adding path to bashrc file"
main_file="main_directory.txt"
main_directory=""
while IFS= read line
do
	echo "$line"
	main_directory=$line
done <"$main_file"
rm -rf main_directory.txt
sudo echo "export PATH=\"$main_directory:$""PATH\"" >> ~/.bashrc
source ~/.bashrc