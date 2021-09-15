#!/bin/bash
currentDir=$PWD
cd "$(dirname "$0")"
MOUNTFROM=$PWD
MOUNTTO='/home/morpheus/workspace/mount'
IMAGE='rsbyrne/risk-portal'
SOCK='/var/run/docker.sock'
echo "starting interactive session"
docker run -v $MOUNTFROM:$MOUNTTO -v $SOCK:$SOCK -it --shm-size 2g $IMAGE bash
echo "finished interactive session"
docker rm $(docker ps -a -q)
cd $currentDir
