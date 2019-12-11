#!/bin/bash
current_dir=$(pwd)


cd api
git pull

cd ../database
git pull

cd ../iot
git pull

cd ../scripts
git pull

cd ../website
git pull


cd ..
source venv/bin/activate
python -m pip install -r scripts/requirements-dev.txt
python -m pip install -e database
python -m pip install -e api
python -m pip install -e iot


cd $current_dir