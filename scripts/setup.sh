#!/bin/bash
distro=$(cat /etc/*-release | grep "DISTRIB_ID=" | cut -d"=" -f2);
privilege=$(whoami);
if [ $privilege = 'root' ]; then
	echo "Root privileges allowed"
	if [ $distro = "Debian" ]; then 
		./debian/setup.sh
  	else
		echo "Setting up Bassa on not Debian bases Linux"
	fi
else
	echo "Run the terminal with root privileges"
	sleep 2
	exit		
fi
