#!/usr/bin/env bash
echo "Installing node modules"
npm install

echo "building dist"
gulp build 

echo "Building Docker"
docker build -t scoreucsc/bassa:ui ./
