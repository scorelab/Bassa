#!bin/bash
cd components/core;
gnome-terminal -e "sudo python3 Main.py";
cd ..;
cd ..;
cd ui/;
gnome-terminal -e "sudo gulp serve";
gnome-terminal -e "sudo aria2c --enable-rpc"
cd ..;
echo "Bassa Running";
