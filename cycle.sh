#!/bin/bash

currentDir=$PWD
cd "$(dirname "$0")"

echo "start main cycle"

./imdo.sh ./imcycle.sh &>> cron.log

echo "end main cycle"

cd $currentDir
