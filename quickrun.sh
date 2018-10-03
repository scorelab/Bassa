#!/bin/sh
# Author : Gaurav Pandey(hcktheheaven)
clear
echo "
██████╗  █████╗ ███████╗███████╗ █████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
██████╔╝███████║███████╗███████╗███████║
██╔══██╗██╔══██║╚════██║╚════██║██╔══██║
██████╔╝██║  ██║███████║███████║██║  ██║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝"

./gulpserve.sh
cd components/core && gnome-terminal -e 'python3 Main.py'
echo "[ Test Server Running... ]"
gnome-terminal -e 'aria2c --enable-rpc'
echo "[ aria2c Running... ]"
echo "[ Gulp Running... ]"
exec sleep 2
