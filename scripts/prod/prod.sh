#!/bin/bash

current_dir=$(pwd)

cd /opt/repos/swarm
sudo cp -va website/dist/swarm-website/. /var/www/html/
python api/main.py &
sleep 10
python iot/examples/computer-monitor.py -s 120 --project demo --device $(hostname)-computer-stats --cache /var/log/iot/vm &

cd $current_dir