#!/bin/sh

YUM=$(which yum)
DNF=$(which dnf)
APT_GET=$(which apt-get)
PACMAN=$(which pacman)
BREW=$(which brew)

# Variable for package manager used by the user
PACKAGE_MANAGER="package_manager"

if ! [ $(id -u) = 0 ]; then
   printf "Please run as root to proceed with installations... \n1. Type in: su\n2. Enter your password\n3. Execute: sh setup.sh\n"

else
   echo "Starting dependency installation..."
   echo "Finding the package manager"

   echo "Installing minio-py libraries"
   git clone https://github.com/minio/minio-py
   cd minio-py
   python setup.py develop
   echo "minio-py libraries installed"

   echo "Installing Minio server locally"
   wget https://dl.min.io/server/minio/release/linux-amd64/minio
   chmod +x minio
   printf "Run as root... \n1. Execute : './minio server /data' to start minio server\n"
   
   if [ ! -z $APT_GET ]; then
      echo -e "apt-get found\n"
      PACKAGE_MANAGER="apt-get"
      ./package-list-aptget

   elif [ ! -z $PACMAN ]; then
      echo -e "pacman found\n"
      PACKAGE_MANAGER="pacman"
      ./package-list-pacman

   elif [ ! -z $DNF ]; then
      echo -e "dnf found\n"
      PACKAGE_MANAGER="dnf"
      ./package-list-dnf

   elif [ ! -z $YUM ]; then
      echo -e "yum found\n"
      PACKAGE_MANAGER="yum"
      ./package-list-yum

   elif [ ! -z $BREW ]; then
      echo -e "brew found\n"
      PACKAGE_MANAGER="brew"
      ./package-list-brew

   else
      echo "Please manually install packages in package-list-$PACKAGE_MANAGER file"
      exit 1
   fi
fi
