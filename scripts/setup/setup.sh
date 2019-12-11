#!/bin/bash


current_dir=$(pwd)

mkdir -p /opt/repos/swarm
cd /opt/repos/swarm

git clone https://github.com/FAU-SWARM/api.git
git clone https://github.com/FAU-SWARM/database.git
git clone https://github.com/FAU-SWARM/iot.git
git clone https://github.com/FAU-SWARM/scripts.git  # the implication being that scripts already exists somewhere
git clone https://github.com/FAU-SWARM/website.git

python3 -m pip install virtualenv
python3 -m virtualenv venv


source venv/bin/activate
python -m pip install -r scripts/requirements-dev.txt
python -m pip install -e database
python -m pip install -e api
python -m pip install -e iot


cd $current_dir