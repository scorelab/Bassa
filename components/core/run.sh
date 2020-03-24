#!/bin/bash

echo "Starting Bassa"
aria2c --enable-rpc & 
python3 Main.py 
