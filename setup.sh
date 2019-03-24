#!/bin/sh

YUM=$(which yum)
DNF=$(which dnf)
APT_GET=$(which apt-get)
PACMAN=$(which pacman)
BREW=$(which brew)

install_yum() {
   # Documented for centOS 7
   # Updating yum
   echo "Setting up yum"
   yum -y update
   yum -y install yum-utils
   yum -y groupinstall development
   echo "yum is ready"

   #Installing Python
   echo "Installing Python"
   yum install centos-release-scl
   yum install rh-python36
   scl enable rh-python36 bash
   python --version
   echo "Python successfully installed"

   #Installing pip
   echo "Installing pip"
   yum install epel-release -y
   yum install python-pip
   echo "pip successfully installed"

   #Installing setup tools
   echo "Installing setuptools"
   wget http://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.6.tar.gz --no-check-certificate
   tar xf setuptools-1.1.6.tar.gz
   cd setuptools-1.1.6
   python3.3 setup.py install
   echo "setuptools installed"

   echo "Installing Aria2"
   yum --enablerepo=rpmforge install aria2 -y
   echo "Aria2 installed"

   echo "Installing mysql-server"
   rpm -ivh https://repo.mysql.com//mysql57-community-release-el7-11.noarch.rpm
   yum install mysql-server -y
   echo "mysql-server installed"

   echo "Installing libmysqlclient"
   yum install mysql-devel -y
   echo "libmysqlclient installed"

   echo "Installing node"
   yum install -y gcc-c++ make
   curl -sL https://rpm.nodesource.com/setup_6.x | sudo -E bash -
   yum install nodejs
   echo "NodeJS installed"

   echo "Installing bower globally"
   npm install -g bower
   echo "bower installed"

   echo "Installing gulp globally"
   npm install -g gulp
   echo "gulp installed"
}

install_dnf() {
   echo "Installing pip"
   dnf install python-pip #Python 2
   dnf install python3    #Python 3
   echo "pip installed"

   echo "Upgrading setuptools"
   dnf upgrade python-setuptools
   echo "setuptools upgraded"

   echo "Installing Aria2"
   yum install aria2
   echo "Aria2 installed"

   echo "Installing mysql-server"
   ## Fedora 29 ##
   dnf install https://dev.mysql.com/get/mysql80-community-release-fc29-1.noarch.rpm
   # choose accordingly
   ## Fedora 28 ##
   #dnf install https://dev.mysql.com/get/mysql80-community-release-fc28-1.noarch.rpm

   ## Fedora 27 ##
   #dnf install https://dev.mysql.com/get/mysql80-community-release-fc27-1.noarch.rpm

   dnf install mysql-community-server
   systemctl start mysqld.service ## use restart after update
   systemctl enable mysqld.service
   echo "mysql-server installed"

   echo "Installing libmysqlclient"
   yum install mysql-devel
   echo "libmysqlclient installed"

   echo "Installing node"
   dnf install -y gcc-c++ make
   curl -sL https://rpm.nodesource.com/setup_10.x | sudo -E bash -
   dnf install nodejs
   echo "NodeJS installed"

   echo "Installing bower globally"
   npm install -g bower
   echo "bower installed"

   echo "Installing gulp globally"
   npm install -g gulp
   echo "gulp installed"
}
install_apt() {
   #!/bin/bash

   echo "Installing pip"
   apt-get install -y python3-pip
   echo "pip installed"

   echo "Installing setuptools"
   apt-get install -y python3-setuptools
   echo "setuptools installed"

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
   curl -sL https://deb.nodesource.com/setup_6.x | -E bash -
   apt-get install -y nodejs
   echo "NodeJS installed"

   echo "Installing bower globally"
   npm install -g bower
   echo "bower installed"

   echo "Installing gulp globally"
   npm install -g gulp
   echo "gulp installed"
}
install_pacman() {
   #updating pacman
   pacman -Syy
   pacman -Su

   echo "Installing python"
   pacman -S python
   echo "pythion installed"

   echo "Installing pip"
   pacman -S python-pip #Python 3
   echo "pip installed"

   echo "Installing setuptools"
   pacman -S python-setuptools
   echo "setuptools installed"

   echo "Installing Aria2"
   pacman -S aria2
   echo "Aria2 installed"

   echo "Installing mariadb"
   pacman -S mariadb
   mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
   systemctl enable mariadb.service
   systemctl start mariadb.service
   mysql_secure_installation
   echo "mariadb installed"

   echo "Installing libmysqlclient"
   pacman -S libmysqlclient
   echo "libmysqlclient installed"

   echo "Installing node"
   pacman -Syyu nodejs
   echo "NodeJS installed"

   echo "Installing bower globally"
   npm install -g bower
   echo "bower installed"

   echo "Installing gulp globally"
   npm install -g gulp
   echo "gulp installed"

}
install_brew() {
   echo "Installing Homebrew"
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   echo "Homebrew Installed"

   echo "Installing python3 and pip"
   brew install python3
   echo "python3 and pip Installed"

   echo "Installing Aria2"
   brew install aria2
   echo "Aria2 Installed"

   echo "Installing and starting MySQL"
   brew install mysql
   brew services start mysql
   echo "MySQL Installed and Started"

   echo "Installing Node"
   brew install node
   echo "Node Installed"

   echo "Installing Bower"
   npm install -g bower
   echo "Bower Installed"

   echo "Installing Gulp"
   npm install -g gulp
   npm install -g gulp-cli
   echo "Gulp Installed"
}

if [ ! -z $APT_GET_CMD ]; then
   install_apt
elif [ ! -z $DNF_CMD ]; then
   install_dnf
elif [ ! -z $YUM_CMD ]; then
   install_yum
elif [ ! -z $PACMAN_CMD ]; then
   install_pacman
elif [ ! -z $BREW ]; then
   install_brew
else
   echo "Failed"
   exit 1
fi
