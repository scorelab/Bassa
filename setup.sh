#!/bin/sh
if ! [ $(id -u) = 0 ]; then
   	printf "Please run as root to proceed with installations... \n1. Type in: su\n2. Enter your password\n3. Execute: sh setup.sh\n"

else
   	echo "Starting Installation..."

	echo "Udating package list and Pre-installed package versions"
	apt-get update && apt-get upgrade
	echo "All packages now updated and ready to be used"

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
	apt-get install -y mysql-server
	echo "mysql-server installed"

	echo "Installing libmysqlclient"
	apt-get install libmysqlclient-dev
	echo "libmysqlclient installed"

	echo "Installing node"
	curl -sL https://deb.nodesource.com/setup_6.x 
	apt-get install -y nodejs
	echo "NodeJS installed"

	echo "Installing bower globally"
	npm install -g bower
	echo "bower installed"

	echo "Installing gulp globally"
	npm install -g gulp
	echo "gulp installed"
fi
