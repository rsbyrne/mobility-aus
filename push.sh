#!/bin/bash
currentDir=$PWD
cd "$(dirname "$0")"
bash configure_ssh.sh
eval "$(ssh-agent)"
ssh-add ~/.ssh/*.pem
git config --global user.email "rohan.byrne@gmail.com"
git config --global user.name "rsbyrne"
git add .
git commit -m "Quick push"
git push -f
cd $currentDir
