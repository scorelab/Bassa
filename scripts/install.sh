#!/bin/bash

echo "=== START OF FILE ==="

echo "==== <Check to see if user is root> ===="
if [ $(whoami) != 'root' ]; then
	echo "Please run this script as root or use sudo"
	exit
fi
echo "==== </Check to see if user is root> ===="
echo

echo "==== <Set path to Bassa directory> ===="
path=$(find ~  -name "Bassa")
echo $path
cd $path
echo "==== </Set path to Bassa directory> ===="
echo

echo "==== <Python change 3.5> ===="
pythonVersion=$(python --version | grep -o "[[:digit:]]\.[[:digit:]]")
if [ $pythonVersion = "3.5" ]; then
   echo "Verified that you are using python 3.5"
else
   rm /usr/bin/python
   ln -s /usr/bin/python3.5 /usr/bin/python
fi
echo "==== </Python change 3.5> ===="
echo

echo "==== <BASSA Setup> ====" 
cd ~/Bassa 
apt-get update # updating system
./setup.sh # run setup script
cd components/core/ 
python setup.py develop 
echo "==== </BASSA Setup> ====" 
echo 

echo "==== <BASSA DB Setup> ===="
export BASSA_DB_USERNAME=root # set the environment variables from DBCon.py 
export BASSA_DB_PASSWORD=Bassa
export BASSA_DB_NAME=Bassa

cd ~/Bassa 
echo "create database Bassa" | mysql -u root -pBassa
mysql -u root -pBassa Bassa < Bassa.sql
echo "==== </BASSA DB Setup> ===="
echo

echo "==== <BASSA UI install> ===="
cd ~/Bassa/ui
npm config set unsafe-perm=true # prevents npm error EACCES: permission denied
npm install
aria2c --daemon  --enable-rpc=true # run as background process
echo "==== </BASSA UI install> ===="
echo

echo "==== <start gulp> ===="
gulp serve # launches Bassa on browser
echo "==== </start gulp> ===="
echo 

echo "==== END OF FILE ===="

