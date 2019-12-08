#!/bin/bash
echo Installing locustio
python3 -m pip install locustio
echo Installing Docker
if [[ "$OSTYPE" == "darwin"* ]];
then
    brew install docker
else
    sudo apt-get install docker
fi
echo Building and running container
cd ../..
echo Building from: $PWD...
docker-compose -f docker-compose.yml up --build
read -p "Done! Press [Enter] to continue..."