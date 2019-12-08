#!/bin/bash
echo Installing locustio
python3 -m pip install locustio

start_locust(){
    echo Starting Locust... Locust will not be ready to use until the Docker container starts.
    locust
    if [ $? -ne 0 ]; then
    echo "Error launching Locust. There may be something wrong with your Python install."
    fi
}

start_bassa(){
    echo Building and running container
    echo Building from: $PWD...
    docker-compose -f ../../../docker-compose.yml up --build
    if [ $? -ne 0 ]; then
        echo "Error launching docker-compose. You may not have docker/docker-compose installed. Please refer to: https://docs.docker.com/install"
    fi
}

start_locust &
start_docker