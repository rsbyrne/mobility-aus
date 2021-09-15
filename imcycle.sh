#!/bin/bash

echo "imcycle start"
python3 fbpull.py
python3 update.py
bash push.sh
echo "imcycle done"
