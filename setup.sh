#!/bin/bash


echo "Finding the package manager"
APT_GET_CMD=$(which apt-get)
PACMAN_CMD=$(which pacman)

if [[ ! -z $APT_GET_CMD ]]; then
    echo -e "apt-get found\n"
    ./package-list-aptget
    
elif [[ ! -z $PACMAN_CMD ]]; then
    echo -e "pacman found\n"
    ./package-list-pacman
else
    echo "Please manually install packages in package-list-aptget file"
    exit 1;
fi